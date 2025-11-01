from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', HomePageView.as_view(), name='home'),
    path("catalog/", include("catalog.urls")),
    path('blog/', include('blog.urls')),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]