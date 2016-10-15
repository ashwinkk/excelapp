from django.conf.urls import url
from leaderboards.views import Top10Scores,PostScore,MyScore
from leaderboards import views

urlpatterns = [
	url(r'postscore/$',PostScore.as_view()),
	url(r'topscores/$',Top10Scores.as_view()),
	url(r'score/(?P<email>.+)/$',MyScore.as_view()),
	url(r'downloadblack/',views.downloadFile),
	url(r'downloadhead/',views.downloadFile2),
	url(r'links/$',views.downloadLinks)
]