from django.conf.urls import url
from .views import Content

urlpatterns = [
	url(r'^$', Content),
]
