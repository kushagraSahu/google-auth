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

@require_POST
def google_auth(request):
	id_token = request.POST.get('idtoken','')
	#for using the tokeninfo endpoint.
	# context = {
	# 	'id_token' = id_token,
	# }
    #return render(request,'account/veriy_id_token.html',context);
	try:
		idinfo = client.verify_id_token(id_token,'433666279275-pba1entmia413ubj9ol6mpl2aknv703q.apps.googleusercontent.com')
    # If multiple clients access the backend server:	
		if (idinfo['aud'] != 433666279275-pba1entmia413ubj9ol6mpl2aknv703q):
			raise crypt.AppIdentityError("Unrecognized client.")
		if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
			raise crypt.AppIdentityError("Wrong issuer.")
	except:
		crypt.AppIdentityError;
    # Invalid token
	userid = idinfo['sub']
