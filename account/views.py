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
from google_auth.settings import GOOGLE_OAUTH2_CLIENT_ID
import json
# Create your views here.

@csrf_exempt
def login(request):
	return render(request, 'account/login.html');

@csrf_exempt
@require_POST
def google_auth(request):
	id_token = request.POST.get('idtoken','')
	print(id_token)
	return render(request,'account/logged_in.html');

@csrf_exempt
@require_POST
def google_login(request):
	info_str = request.POST.get('info','')
	import json
	json_acceptable_string = info_str.replace("'", "\"")
	info = json.loads(json_acceptable_string)
	print("//////////////////////////////////////////////////  \n ")
	print(info)
	print(" \n ")
	userID = info['sub']
	email = info['email']
	user = MyUser.objects.filter(email = email)
	user.is_active = info['email_verified']
	if user:
		#if info['aud'] == GOOGLE_OAUTH2_CLIENT_ID:
			if info['iss'] in ['accounts.google.com', 'https://accounts.google.com']:
				if user.is_active == True:
					auth_login(request,user)
				else:
					return {"status":"error","code":501,"message":"Inactive User"};
			else:
				return {"status":"error","code":502,"message":"Wrong issuer"};
		#else:
		#	return {"status":"error","code":503,"message":"Unrecognized client"};
	#First Time User
	else:
		user = None
		firstname = info['given_name']
		lastname = info['family_name']
		username = email.split('@')[0]
		password = username + userID
		print("/////" + password + "/////")
		user = MyUser.objects.create(username = username, first_name = firstname, last_name = lastname, email = email)
		user.set_password(password)
		user.save()
		user.backend='django.contrib.auth.backends.ModelBackend'
		auth_login(request,user)

	response = {
		'user' : user,
	}	
	return response




