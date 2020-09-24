
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('Registration',views.Registration, name = "Registration" ),
    path('Login',views.Login, name = "Login" ),
    path('Logout',views.Logout, name = "Logout" ),
    path('SetPassword',views.SetPassword, name = "SetPassword" ),
    path('UserProfil',views.UserProfil, name = "UserProfil" ),
    path('UpdateProfile',views.UpdateProfile, name = "UpdateProfile" ),
    path('MoreDetails/<int:id>',views.MoreDetails, name = "MoreDetails" ),
    
    
    


    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
