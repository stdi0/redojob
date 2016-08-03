# -*- coding:utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django import forms
from django.contrib import auth

from .models import Job, User
from .forms import RegistrationForm, LoginForm, AddingPosition, SearchForm

# Create your views here.

def index(request):
    result = []
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            r = form.cleaned_data.get('text')
            if not r:
                pass
            else:
                flag = True
                result = Job.objects.filter(name__icontains=r)
                context = {'result': result, 'search_form': form, 'flag': flag}
                return render(request, 'core/index.html', context)
    else:
        form = SearchForm()
            #return render(request, 'core/ .html', context)
    latest_jobs_list = Job.objects.all()[::-1]
    context = {'latest_jobs_list': latest_jobs_list, 'search_form': form}
    return render(request, 'core/index.html', context)

def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'core/detail.html', {'job': job})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponse("/Ok/")
    else:
        form = RegistrationForm()
    return render(request, "core/register.html", {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('core:index', args=()))
    else:
        form = LoginForm()
    return render(request, "core/login.html", {'form': form})

def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('core:index', args=()))

def adding_position(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('core:login', args=()))
    if request.method == 'POST':
        form = AddingPosition(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            employer = form.cleaned_data.get('employer')
            salary = form.cleaned_data.get('salary')
            text = form.cleaned_data.get('text')
            avatar = form.cleaned_data.get('image')
            phone = form.cleaned_data.get('phone')
            u = User.objects.get(username=request.user.username)
            j = u.job_set.create(name=name, employer=employer, salary=salary, text=text, avatar=avatar, phone=phone)
            #j = Job(name=name, employer=employer, salary=salary, text=text, avatar=avatar)
            #j.save()
            return HttpResponseRedirect(reverse('core:detail', args=(j.id,)))
    else:
        form = AddingPosition()
    return render(request, 'core/adding_position.html', {'form': form})

def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('core:login', args=()))
    profile_jobs_list = Job.objects.filter(author__username=request.user.username)
    context = {'profile_jobs_list': profile_jobs_list}
    return render(request, "core/profile.html", context)

def delete(request, job_id):
    try:
        d = Job.objects.filter(pk=job_id)
        d.delete()
    except:
        pass
    return HttpResponseRedirect(reverse('core:profile', args=()))




