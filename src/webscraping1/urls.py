
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('abc/', include('scraper.urls')),
    path('data/', TemplateView.as_view(template_name='scraper1/index.html')),
]
