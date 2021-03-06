"""MovieProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework.documentation import include_docs_urls
# from rest_framework_swagger.views import get_swagger_view

#describe project level urls

# schema_view = get_swagger_view(title='Movie Operations API')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('main/',include('movie_app.urls')),
    path('', include_docs_urls(
    	title='Movies REST API', public=True, authentication_classes=[], permission_classes=[]
	)),
    # url(r'^$', schema_view)
]
