from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from .views import VideoApiView

urlpatterns = [
    path('api/v1/videos/',VideoApiView.as_view({'get':'list','post':'create'})),
    path('api/v1/video/<int:pk>/',VideoApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]