from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from car.models import Car, Comment


class CarMixin(LoginRequiredMixin):
    error_message = None
    model = Car

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        car = Car.objects.filter(id=self.kwargs["pk"], owner=self.request.user).first()
        if not car:
            messages.error(self.request, self.error_message)
            return redirect(reverse_lazy("car_detail", kwargs={"pk": self.kwargs["pk"]}))

        return super().dispatch(request, *args, **kwargs)


class CarListView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"


class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"
    context_object_name = "car"

    def get_queryset(self):
        return Car.objects.filter(id=self.kwargs["pk"]).prefetch_related("comments__author")

class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ["make", "model", "year", "description"]
    template_name = "car_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("car_detail", kwargs={"pk": self.object.id})


class CarUpdateView(CarMixin, UpdateView):
    error_message = "You cannot edit this car."
    fields = ["make", "model", "year", "description"]
    template_name = "car_form.html"

    def get_success_url(self):
        return reverse_lazy("car_detail", kwargs={"pk": self.kwargs["pk"]})


class CarDeleteView(CarMixin, DeleteView):
    error_message = "You cannot delete this car."
    success_url = reverse_lazy("cars")
    template_name = "car_delete.html"


class CommentListView(ListView):
    model = Comment
    template_name = "comments.html"
    context_object_name = "comments"

    def get_queryset(self):
        return Comment.objects.filter(car=self.kwargs["car_id"])


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["content"]
    template_name = "comment_form.html"

    def form_valid(self, form):
        car = Car.objects.get(id=self.kwargs["car_id"])
        form.instance.author = self.request.user
        form.instance.car = car

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("car_detail", kwargs={"pk": self.object.car.id})
