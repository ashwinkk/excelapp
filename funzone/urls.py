from django.conf.urls import url

from funzone.views import UserScoreView,TopScores,PostScore

urlpatterns = [
	url(r'topscores/$',TopScores.as_view()),
	url(r'score/(?P<email>.+@[\w]+\.[\w]+)/$',UserScoreView.as_view()),
	url(r'postscore/$',PostScore.as_view())
]