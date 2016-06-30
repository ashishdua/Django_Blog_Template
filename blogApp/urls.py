from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	url(r'^$',views.blog_list),
	url(r'(?P<pk>\d+)/$',views.blog_detail , name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)