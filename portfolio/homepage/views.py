from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime
from django.core.mail import send_mail
import re
from django.template.loader import render_to_string, get_template
from django.conf import settings as django_settings
from homepage import models as mod
from django.db.models import Q
from django.contrib.auth.models import Permission, Group


def index(request):


    return render(request, 'homepage/index.html')

def sawtooth(request):


    return render(request, 'homepage/sawtooth.html')

def mentors(request):


    return render(request, 'homepage/mentors.html')
