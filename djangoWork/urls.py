"""djangoWork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.core.mail import send_mail
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('signup', views.signup, name='signup'),
    path('feedback', views.feedback, name= 'feedback'),
    path('restaurants', views.restaurants, name= 'restaurants'),
    path('EAST-EAST_ASIAN_SPICE_TRAIL', views.EASTEASTASIANSPICETRAIL, name='EAST-EAST_ASIAN_SPICE_TRAIL'),
    path('THE_EARTH_PLATE', views.THEEARTHPLATE, name='THE_EARTH_PLATE' ),
    path('KEBABS_AND_KURRIES', views.KEBABSANDKURRIES, name='KEBABS_AND_KURRIES'),
    path('NAMAK', views.NAMAK, name='NAMAK'),
    path('PESHAWRI', views.PESHAWRI, name='PESHAWRI'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name= 'password_reset.html'), name= 'password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'password_reset_done.html'), name= 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'password_reset_confirm.html'), name= 'password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'password_reset_complete.html'), name= 'password_reset_complete'),
    path('other', views.other, name='other'),
    path('restaurant_analysis_1', views.restaurant_analysis_1, name='restaurant_analysis_1'),
    path('restaurant_analysis_2', views.restaurant_analysis_2, name='restaurant_analysis_2'),
    path('restaurant_analysis_3', views.restaurant_analysis_3, name='restaurant_analysis_3'),
    path('restaurant_analysis_4', views.restaurant_analysis_4, name='restaurant_analysis_4'),
    path('restaurant_analysis_5', views.restaurant_analysis_5, name='restaurant_analysis_5'),
    
    # URL NAVIGATION FOR RESTAURNTS
    path('restaurants/EAST-EAST_ASIAN_SPICE_TRAIL', views.EASTEASTASIANSPICETRAIL, name='EAST-EAST_ASIAN_SPICE_TRAIL'),
    path('restaurants/THE_EARTH_PLATE', views.THEEARTHPLATE, name='THE_EARTH_PLATE' ),
    path('restaurants/KEBABS_AND_KURRIES', views.KEBABSANDKURRIES, name='KEBABS_AND_KURRIES'),
    path('restaurants/NAMAK', views.NAMAK, name='NAMAK'),
    path('restaurants/PESHAWRI', views.PESHAWRI, name='PESHAWRI'),
    
    # URL NAVIGATION FOR RESTAURANT ANALYSIS
    path('restaurants/restaurant_analysis_1', views.restaurant_analysis_1, name='restaurant_analysis_1'),
    path('restaurants/restaurant_analysis_2', views.restaurant_analysis_2, name='restaurant_analysis_2'),
    path('restaurants/restaurant_analysis_3', views.restaurant_analysis_3, name='restaurant_analysis_3'),
    path('restaurants/restaurant_analysis_4', views.restaurant_analysis_4, name='restaurant_analysis_4'),
    path('restaurants/restaurant_analysis_5', views.restaurant_analysis_5, name='restaurant_analysis_5')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
