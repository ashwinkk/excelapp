from django.conf.urls import url

from .views import UploadImage,ViewImages,LikeImage
from gallery import views

urlpatterns = [
	url(r'album/$',ViewImages.as_view()),
	url(r'upload/$',UploadImage.as_view()),
	url(r'like/$',LikeImage.as_view()),
	url(r'cache/$',views.cacheImages),
	url(r'$',views.approveImage)
]