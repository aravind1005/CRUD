from django.urls import path
from .views import Model
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Model.home, name="home"),
    path('uploadfile/', Model.uploadfile, name="uploadfile"),
    path('deletefile/<int:id>/', Model.deleteFile, name="deletefile"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
