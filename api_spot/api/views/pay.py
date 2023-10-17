from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.exceptions import OrderStatusError
from api.permissions import IsOwnerOrReadOnly
# from api.serializers.pay import PaySerializer
from api.services.orders import order_finished_email
from spots.constants import PAID, WAIT_PAY
from spots.models import Order


@extend_schema(
    tags=('pay',),
)
class PayView(APIView):
    """
    Оплачивание заказа(изменения статуса).
    """
    permission_classes = (IsOwnerOrReadOnly, )
    serializer_class = None

    def patch(
            self, request, location_id: int, spot_id: int, order_id: int
    ) -> Response:
        """Метод patch, для оплачивания заказа."""
        # serializer = PaySerializer(
        #     data=request.data,
        #     context={
        #         'order_id': order_id,
        #         'location_id': location_id,
        #         'spot_id': spot_id
        #     }
        # )
        # serializer.is_valid(raise_exception=True)
        # order = serializer.validated_data.get('order')
        order = get_object_or_404(
            Order,
            id=order_id,
            spot=spot_id,
            spot__location=location_id
        )
        self.check_object_permissions(request, order)
        if order.status != WAIT_PAY:
            raise OrderStatusError
        order.status = PAID
        order.save()
        order_finished_email(order)
        return Response(
            # serializer.data,
            {'message': 'Заказ оплачен'},
            status=status.HTTP_200_OK
        )
