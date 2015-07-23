from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import principal

urlpatterns = [
    # Examples:
    # url(r'^$', 'CRUD_Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('principal.urls')),
    url(r'^', include('catalogos.urls')),
]
