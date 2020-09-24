from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
path('sms/<int:id>', views.message, name="sms"),
path('statut', views.statut, name="statut"),
path('Bot',views.Bot, name = "Bot" ),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)