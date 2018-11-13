"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import home_page,user_login,admin_login,register_page,details_page,no_details,no_schemes,apply,success_page,scheme_page
from user.views import details_review,details_view,scheme_view,review_request
from django.contrib.auth import logout

urlpatterns = [
	url(r'^login/$',user_login,name="LoginPage"),
    url(r'^admin_login/$',admin_login,name="AdminLogin"),
	url(r'^register/$',register_page,name="RegisterPage"),
	url(r'^$',home_page,name="Home"),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$',logout,{"template_name": 'home.html'}),
    url(r'^add-details/$',details_page,name="DetailsPage"),
    url(r'^view_page/$',details_view,name="DetailsView"),
    url(r'^view_schemes/$',scheme_view,name="SchemeView"),
    url(r'^no-details/$',no_details,name="NoDetails"),
    url(r'^no-schemes/$',no_schemes,name="NoScheme"),
    url(r'^apply/$',apply,name="Apply"),
    url(r'^success/$',success_page),
    url(r'^review/$',review_request,name="ReviewRequest"),
    url(r'^detail/(?P<name>\w+)/$', details_review, name="ReviewDetail"),
    url(r'^add-schemes/$',scheme_page,name="AddScheme")

]
