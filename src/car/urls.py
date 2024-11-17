from django.urls import include, path
from car import views


urlpatterns = [
    path("", views.CarListView.as_view(), name="cars"),
    path("add/", views.CarCreateView.as_view(), name="car_add"),
    path("<int:pk>/", views.CarDetailView.as_view(), name="car_detail"),
    path("<int:pk>/edit/", views.CarUpdateView.as_view(), name="car_edit"),
    path("<int:pk>/delete/", views.CarDeleteView.as_view(), name="car_delete"),

    path("<int:car_id>/comments/", views.CommentListView.as_view(), name="comment_list"),
    path("<int:car_id>/comment/add/", views.CommentCreateView.as_view(), name="add_comment"),
]
