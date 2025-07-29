from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import  UsernameOrEmailAuthenticationForm,ForgotPasswordForm,SetNewPasswordForm,CustomUserCreationForm
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UsernameOrEmailAuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username_or_email = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                User = get_user_model()
                try:
                    if '@' in username_or_email:
                        user = User.objects.get(email=username_or_email)
                    else:
                        user = User.objects.get(username=username_or_email)
                except User.DoesNotExist:
                    if '@' in username_or_email:
                        form.add_error('username', "This email is not registered.")
                    else:
                        form.add_error('username', "This username does not exist.")
                else:
                    user = authenticate(request, username=user.username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('/')
                    else:
                        form.add_error('password', "The password is incorrect.")
        else:
            form = UsernameOrEmailAuthenticationForm()

        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
# views.py
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'your account has been created.')
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'your account didnt create.')
        form = CustomUserCreationForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')