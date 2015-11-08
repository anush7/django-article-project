from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings as mysettings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^articles/', include('article.urls')),

    url(r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': mysettings.MEDIA_ROOT}),
    #url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': mysettings.STATIC_ROOT}),

]
