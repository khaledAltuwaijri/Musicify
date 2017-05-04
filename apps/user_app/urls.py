from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^register$', register, name="register"),
    url(r'^login$', login, name="login"),
    url(r'^profile$', profile, name="profile"),
    url(r'^edit_profile$', edit_profile, name="edit_profile"),
    url(r'^update_profile$', update_profile, name="update_profile"),
    url(r'^logout$', logout, name="logout"),
    url(r'^follow_users$', follow_users, name="follow_users"),
    url(r'^follow/(?P<followee_id>\d+)/$', follow, name="follow"),
    url(r'^unfollow/(?P<followee_id>\d+)/$', unfollow, name="unfollow"),
    url(r'^my_followers$', my_followers, name="my_followers"),
    url(r'^follower_profile/(?P<follower_id>\d+)$', follower_profile, name="follower_profile"),
]
