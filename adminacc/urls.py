from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$',views.chat),
	url(r'logout/$',views.logout),
]