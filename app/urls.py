from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('download/', views.DownloadData.as_view(), name='download_data'),
    path('upload/', views.UploadOrdersView.as_view(), name='upload_data'),
    path('api/v1/download-endpoint/', views.DownloadApiView.as_view(), name='download_api_endpoint'),
    path('api/v1/upload-orders/', views.UploadOrdersAPIView.as_view(), name='upload_orders_api'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
