from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (FavoriteViewSet, OrderGetViewSet, OrderViewSet,
                    ReviewCreateViewSet, ReviewGetViewSet,
                    LocationViewSet, UserViewSet, SpotViewSet)


app_name = 'api'

router_api_v1 = DefaultRouter()

router_api_v1.register(r'users', UserViewSet, basename='users')

router_api_v1.register(
    r'locations/(?P<location_id>\d+)/spots/(?P<spot_id>\d+)'
    r'/order/(?P<order_id>\d+)/reviews',
    ReviewCreateViewSet,
    basename='review'
)
router_api_v1.register(
    r'locations/(?P<location_id>\d+)/reviews',
    ReviewGetViewSet,
    basename='get_reviews'
)

router_api_v1.register(
    r'locations/(?P<location_id>\d+)/favorite',
    FavoriteViewSet,
    basename='favorite'
)
router_api_v1.register(
    r'locations/(?P<location_id>\d+)/spots/(?P<spot_id>\d+)/order',
    OrderViewSet,
    basename='order'
)
router_api_v1.register(
    'orders',
    OrderGetViewSet,
    basename='get_orders'
)
router_api_v1.register(
    r'locations',
    LocationViewSet,
    basename='favorite'
)
router_api_v1.register(
    r'locations/(?P<location_id>\d+)/spots',
    SpotViewSet,
    basename='spots'
)

urlpatterns = [
    path('v1/', include(router_api_v1.urls)),
    path('v1/auth/', include('djoser.urls.authtoken')),
]
