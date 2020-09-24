
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('Publication/',views.Publication, name = "Publication" ),
    path('LikePost/',views.LikePost, name = "LikePost" ),
    path('Publication/<int:id>',views.PublicationDetails, name = "PublicationDetails" ),

    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
