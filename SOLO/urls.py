from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'division', DivisionViewSet)
router.register(r'position', PositionsViewSet)
router.register(r'vocation', VocationViewSet)
router.register(r'interest', InterestCreateViewSet)
# router.register(r'organizations', OrganizationViewSet)
# router.register(r'inventory', InventoryViewSet)
# router.register(r'categories', CategoryViewSet)
# router.register(r'event-types', EventTypeViewSet)
# router.register(r'organization-members-for-users', MembersInOrganizationForUserViewSet)
# router.register(r'organization-members-for-organizations', MembersInOrganizationForOrganizationViewSet)
# router.register(r'event-guests', EventGuestsForUserViewSet)
# router.register(r'slides', SlideViewSet)

urlpatterns = [
    # DRF router
    path('', include(router.urls)),
    # djoser auth urls
    url(r'^auth/', include('djoser.urls')),
    # djoser auth jwt urls
    url(r'^auth/', include('djoser.urls.jwt')),
    # Активация профиля пользователя
    path('activate/<str:uid>/<str:token>/', UserActivationView.as_view()),
    path('leader-check/', LeaderCheck.as_view()),
    # Смена пароля пользователя
    path('password/reset/confirm/<str:uid>/<str:token>/', PasswordResetConfirmView.as_view()),
    # Логин GUI DRF
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
