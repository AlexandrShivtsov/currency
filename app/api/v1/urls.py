from api.v1 import views

from django.urls import path

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'api'


router = DefaultRouter()
router.register(r'rates', views.RateViewSet, basename='rate')
router.register(r'contact_us', views.ContactUsView, basename='contact_us')
urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('choices/',  views.RateChoicesView.as_view(), name='currency-choices'),
    path('banks/',  views.SourceBankView.as_view(), name='banks'),
    path('contact_us_list/', views.ContactUsList, name='contact_us_list'),
    path('contact_us_create/', views.CreateContactUs, name='contact_us_create'),
    path('contact_us_update/<str:pk>/', views.UpdateContactUs, name='contact_us_update'),
    path('contact_us_delete/<str:pk>/', views.DeleteContactUs, name='contact_us_delete'),

]

urlpatterns.extend(router.urls)
