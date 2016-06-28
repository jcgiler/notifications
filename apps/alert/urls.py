from django.conf.urls import url
from .views import ContentView

urlpatterns = [
	url(r'^$', ContentView.as_view(), name="index"),
]
