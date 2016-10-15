from django.conf.urls import url
from .views import Userslist,Userdefs
from userapp import views

urlpatterns=[
	# url(r'^$',Userslist.as_view()),
	url(r'signup/$',Userdefs.as_view()),
]