from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('download/', views.DownloadData.as_view(), name='download_data'),
    path('api/v1/download-endpoint/', views.DonwloadApiView.as_view(), name='download_api_endpoint'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
