from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from MyCollegeEdrp import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    url('college/', include("college.urls")),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url('^$', RedirectView.as_view(url='college/')),
    url(r'^captcha/', include('captcha.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
