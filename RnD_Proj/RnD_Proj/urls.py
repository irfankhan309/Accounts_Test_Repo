from django.contrib import admin
from django.urls import path,include
from TestApp import urls
from Accounts import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('TestApp.urls')),
    path('',include('Accounts.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),


]
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
