from django.conf import settings
from django.contrib import admin
from django.urls import re_path
from django.views.generic import TemplateView
from django.views.static import serve
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', HomePageView.as_view(), name='home'),
    path('', include('catalog.urls')),
    path("catalog/", include("catalog.urls")),
    path("blog/", include("blog.urls")),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("users/", include("users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
