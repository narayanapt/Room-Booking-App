from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

app_name = 'room_booking'

urlpatterns = [
	path('',user_views.index,name="index"),
	path('register/',user_views.register,name="register"),
	path('login/',auth_views.LoginView.as_view(template_name = "room_booking/login.html"),name = "login"),
	path('logout/',auth_views.LogoutView.as_view(template_name = "room_booking/logout.html"),name = "logout"),
	path('user_home/',user_views.user_home,name="user-home"),
	path('bookings/',user_views.bookings,name="bookings"),
]