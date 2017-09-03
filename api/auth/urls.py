"""api.auth.urls"""

from django.conf.urls import url
from api.auth import views

urlpatterns = [
    url(r'^me/?$', views.UserView.as_view(), name='user'),
    url(r'^me/profile/?$', views.ProfileView.as_view(), name='profile'),
    url(r'^login/?$', views.LoginView.as_view(), name='login'),
    url(r'^logout/?$', views.LogoutView.as_view(), name='logout'),
    url(r'^register/?$', views.RegisterView.as_view(), name='register'),
]
