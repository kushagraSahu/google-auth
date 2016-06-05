from django.conf.urls import url
from .views import login, google_auth, google_login
urlpatterns = [
    url(r'^login/$',login, name = "login"),
    url(r'^google-auth/$',google_auth, name = "google_auth"),
    url(r'^google-login/$',google_login, name = "google_login"),
]