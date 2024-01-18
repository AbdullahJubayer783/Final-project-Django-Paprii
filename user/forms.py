from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm

class RegestrationsForm(UserCreationForm):
    first_name = forms.CharField(widget= forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={'id': 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name' , 'email']
        # fields = ['username','first_name','last_name' , 'email','password']
        def save(self):
            username = self.cleaned_data['username']
            first_name = self.cleaned_data['first_name']
            last_name = self.cleaned_data['last_name']
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            confirm_password = self.cleaned_data['confirm_password']

            if password != confirm_password:
                raise forms.ValidationError({'error':"Password dosn't matched!"})
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError({'error':"Email already exists!"})
            account = User(username=username,email=email,first_name=first_name,last_name=last_name)
            user = forms.save(commit=False)        
            user.is_active = False 
            user.save()
            # print(account)
            account.set_password(password)
            account.is_active = False
            account.save()
            return account

class UserDataChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']