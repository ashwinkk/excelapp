from django.conf.urls import url
from .views import FeedList,FeedUpdates

urlpatterns = [
	url(r'^$',FeedList.as_view()),
	url(r'^(?P<timestring>[\d]+-[\d]+-[\d]+T[\d]+:[\d]+:[\d]+[\.]*[\d]+)/$',FeedUpdates.as_view()),
]