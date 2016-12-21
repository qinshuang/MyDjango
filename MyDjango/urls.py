from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

# from django.contrib import admin


# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'MyDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include('admin.urls')),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
