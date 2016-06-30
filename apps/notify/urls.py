from django.conf.urls import url
from .views import Content, Confirm

urlpatterns = [
        url(r'^confirm/', Confirm),
	url(r'^', Content),
]
