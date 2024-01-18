from typing import Any
from django.shortcuts import render , redirect
from django.views.generic import FormView 
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import RegestrationsForm , UserDataChangeForm
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.contrib.auth import login , logout
from django.contrib.auth.views import LogoutView 
from .models import OrderDetails
from django.views.generic import CreateView , UpdateView , DeleteView , DetailView
# Create your views here.

class UserCreationView(FormView):
    template_name = 'user_registration.html'
    form_class = RegestrationsForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        token = default_token_generator.make_token(user)
        print("token",token)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        print("uid",uid)
        confirm_link = f"http://127.0.0.1:8000/user/register/{uid}/{token}"
        email_subject = "Confirm Your Email"
        email_body = render_to_string('confirm_email.html',{'confirm_link' : confirm_link})
        email = EmailMultiAlternatives(email_subject,'',to=[user.email])
        email.attach_alternative(email_body,"text/html")
        email.send()
        # login(self.request,user)
        return super().form_valid(form)
    
def activate(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        # login(request,user)
        return redirect("home")
    else:
        return redirect("register") 


class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self) :
        return reverse_lazy("home")

class UserLogoutview(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy("home")

class UserProfileView(UpdateView):
    model = User
    form_class = UserDataChangeForm
    template_name = 'profile.html'
    success_url = reverse_lazy('profile') 

    def get_object(self, queryset=None):
        return self.request.user
    def form_valid(self, form):
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history'] = OrderDetails.objects.filter(user=self.request.user)
        return context
# class UserProfileView(DetailView):
#     model = User
#     template_name = 'profile.html'
#     # pk_url_kwarg = 'id'
#     context_object_name = 'user'

#     def get_object(self, queryset=None):
#         return self.request.user

#     def form_valid(self, form):
#         return super().form_valid(form)
    # class ProfileUpdateView(UpdateView):
#     model = UserAccountModel
#     form_class = UserDataChangeForm
#     template_name = 'profile.html'
#     success_url = reverse_lazy('profile') 
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['objects'] = BorrowBookModel.objects.all()
    #     return context 
# class RegistrationFormView()
#     def post(self,request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             print(user)
            
            
#             return Response("Check Your Mail For Confirmation..")
#         return Response(serializer.errors)