from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import include, path

from src.views import HomePageView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path("auth/", include("custom_auth.urls")),
    path("car/", include("car.urls")),

    path("api/", include("car.api.urls"))
] + debug_toolbar_urls()
