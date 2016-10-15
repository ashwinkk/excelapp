from django.conf.urls import url
from .views import EventList

urlpatterns = [
	url(r'(?P<department>\w\w)/$',EventList.as_view()),	
]