from django.urls import reverse_lazy
from django.views.generic import FormView

from custom_auth.forms import RegisterForm


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
