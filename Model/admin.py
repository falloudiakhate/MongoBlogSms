from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(Message)
admin.site.register(Publication)
admin.site.register(Comments)
admin.site.register(Statut)
admin.site.register(Post)