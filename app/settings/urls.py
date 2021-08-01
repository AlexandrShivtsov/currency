"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from currency.views import contact_us
from currency.views import create_source
from currency.views import delete_source
from currency.views import details_source
from currency.views import hello_world
from currency.views import index
from currency.views import login
from currency.views import source_list
from currency.views import update_source


from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', login),
    path('hello-world/', hello_world),
    path('contactus/', contact_us),
    path('source-list/', source_list),
    path('source-list/create-source/', create_source),
    path('source-list/details-source/<int:source_id>/', details_source),
    path('source-list/update-source/<int:source_id>/', update_source),
    path('source-list/delete-source/<int:source_id>/', delete_source),
]
