from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

app_name = 'core'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<job_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^add/$', views.adding_position, name='add'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^delete/(?P<job_id>[0-9]+)/$', views.delete, name='delete'),
]


