from django.urls import path, reverse_lazy
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from accounts.views import register_as_customer, register_as_seller, profile_seller, subscribe
from django.conf.urls import url


urlpatterns = [ 
    path('register/customer/', register_as_customer, name='register_as_customer'),
    path('register/seller/', register_as_seller, name='register_as_seller'),
    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/seller/', profile_seller, name='profile_seller'),
    path('profile/seller/subscribe', subscribe, name='subscribe'),
    
    
    path('accounts/password-reset/', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done'), 'template_name': 'accounts/password_reset_form.html'}, name='password_reset'),
    path('accounts/password-reset/done/', password_reset_done, {'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete'), 'template_name': 'accounts/password_reset_confirm.html'}, name='password_reset_confirm'),
    path('accounts/password-reset/complete/', password_reset_complete, {'template_name': 'accounts/password_reset_complete.html'}, name='password_reset_complete'),
]