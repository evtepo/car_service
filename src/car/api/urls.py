from django.urls import include, path


urlpatterns = [
    path("v1/", include("car.api.v1.urls")),
]
