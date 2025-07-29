from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    #     login
    path('logout/', views.logout_view, name='logout'),
    #     logout
    path('signup/', views.signup_view, name='signup'),
    #     registeration . singup
    # آدرس های مربوط به ریست پسورد
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html', # تمپلت خودتون رو مشخص کنید
        email_template_name='registration/password_reset_email.html', # تمپلت ایمیل رو مشخص کنید
        subject_template_name='registration/password_reset_subject.txt' # تمپلت موضوع ایمیل رو مشخص کنید
        ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html' # تمپلت خودتون رو مشخص کنید
        ), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html' # تمپلت خودتون رو مشخص کنید
        ), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html' # تمپلت خودتون رو مشخص کنید
        ), name='password_reset_complete'),
]
