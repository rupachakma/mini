from django.contrib import admin
from django.urls import path

from Blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="homepage"),
    path('signuppage/', views.signuppage,name="signuppage"),
    path('loginpage/', views.loginpage,name="loginpage"),
    path('dashboardpage/', views.dashboardpage,name="dashboardpage"),
    path('contactpage/', views.contactpage,name="contactpage"),
    path('aboutpage/', views.aboutpage,name="aboutpage"),
    path('logout/', views.logout,name="logout"),
]
