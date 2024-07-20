from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import Http404
from django.views.generic import CreateView, UpdateView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework import generics, permissions

from basta_hua_sasta.account.models import UserDetails
from basta_hua_sasta.account.serializers import UserDetailsSerializer


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("homepage")
    template_name = "account/registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        auth.login(self.request, self.object)
        UserDetails.objects.create(user=self.object)
        return response

class LogInView(LoginView):
    template_name = "account/registration/login.html"

class LogOutView(LogoutView):
    template_name = "account/registration/logout.html"

class ProfileDetailView(LoginRequiredMixin, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserDetailsSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get_object(self):
        try:
            return UserDetails.objects.get(user=self.request.user)
        except UserDetails.DoesNotExist:
            raise Http404("No such user exists")

    def get(self, request, *args, **kwargs):
        return Response(super().get(request, *args, **kwargs).data,
                        template_name='account/detail.html')

class ProfileAddressUpdateView(UpdateView):
    model = UserDetails
    fields = ['city', 'state', 'zip', 'address']
    success_url = reverse_lazy('account:profile-detail')
    template_name = 'account/form.html'
    slug_field = 'user_id'
    slug_url_kwarg = 'user_id'

class ProfileUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('account:profile-detail')
    template_name = 'account/form.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
