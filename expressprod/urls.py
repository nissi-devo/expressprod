from django.contrib import admin
from django.urls import path,include

urlpatterns = [

    #Django Admin
    path("admin/", admin.site.urls),

    #User management
    path("accounts/", include("django.contrib.auth.urls")),

    #Local app
    path("", include("store.urls"))

    
]
