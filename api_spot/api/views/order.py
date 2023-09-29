import datetime

from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from api.services.orders import order_confirmation_email, order_cancel_email
from api.filters import OrderFilter
from api.mixins import CreateUpdateViewSet, RetrieveListViewSet
from api.permissions import IsOwnerOrReadOnly
from api.serializers.order import OrderSerializer, OrderUpdateSerializer
from api.tasks import change_status_task, close_status_task
from spots.models import Order
from spots.constants import CANCEL, PAID, WAIT_PAY


@extend_schema(
    tags=('orders',)
)
class OrderViewSet(CreateUpdateViewSet):
    """
    Представление создания заказов и изменение статуса для отмены.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'update':
            return OrderUpdateSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        instance = serializer.save()
        change_status_task.apply_async(
            args=[instance.id], countdown=settings.TIME_CHANGE_STATUS
        )
        order_confirmation_email(instance)
        finish_time = instance.date_finish
        countdown = (finish_time - datetime.datetime.now()).total_seconds()
        close_status_task.apply_async(
            args=[instance.id], countdown=countdown
        )

    def perform_update(self, serializer):
        instance = serializer.instance
        if instance.status == PAID:
            instance.status = CANCEL
            instance.save()
            order_cancel_email(instance)
        if instance.status == WAIT_PAY:
            instance.status = CANCEL
            instance.save()


class OrderGetViewSet(RetrieveListViewSet):
    """
    Представление заказов авторизованного пользователя с возможностью
    фильтрации по статусу "завершен".
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter)
    filterset_class = OrderFilter
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = PageNumberPagination

    def get_queryset(self):
        """Получение выборки с заказами для текущего пользователя."""
        if self.request.user.is_authenticated:
            return super().get_queryset().filter(user=self.request.user)
        return super().get_queryset()
