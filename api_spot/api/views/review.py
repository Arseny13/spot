from django.shortcuts import get_object_or_404

from api.mixins import CreateDestroyViewSet, RetrieveListViewSet
from api.serializers.review import ReviewSerializer
from spots.models.order import Order
from spots.models.review import Review
from spots.models.spot import Spot


class ReviewCreateViewSet(CreateDestroyViewSet):
    """Вьюсет модели отзывов для создания и удаления."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_order(self):
        """Получение текущего объекта (заказа)."""
        return get_object_or_404(Order, pk=self.kwargs.get('order_id'))

    def get_queryset(self):
        """Получение выборки с отзывами текущей брони."""
        return self.get_order().reviews.all()


class ReviewGetViewSet(RetrieveListViewSet):
    """Вьюсет модели отзывов для получения."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_spot(self):
        """Получение текущего объекта ()."""
        return get_object_or_404(Spot, pk=self.kwargs.get('spot_id'))

    def get_queryset(self):
        """Получение выборки с отзывами текущего спота."""
        return Review.objects.filter(booked_spot__spot=self.get_spot())
