from django.conf.urls import url
from .views import login, google_auth
urlpatterns = [
    url(r'^login/$',login, name = "login"),
    url(r'^google_auth/$',google_auth, name = "google_auth"),
]