from django.urls import path

from .views import CarListView, CarDetailView, CommentView


urlpatterns = [
    path("car/", CarListView.as_view()),
    path("car/<int:car_id>/", CarDetailView.as_view()),
    path("comment/<int:car_id>/", CommentView.as_view()),
]
