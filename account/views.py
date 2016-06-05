from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import MyUser
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template import loader
from django.core import serializers
# Create your views here.

def login(request):
	return render(request, 'account/login.html');

@require_http_methods(['GET','POST'])
def google_auth(request):
	pass