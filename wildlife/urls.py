from django.conf.urls import patterns, include, url
from wildlife import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'targoviste_wildlife_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<username_slug>[\w\-]+)/$', views.user_profile, name='profile'),
    url(r'^post/(?P<post_slug>[\w\-]+)/$', views.post, name='post'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^add_post/$', views.add_post, name='add_post'),
    url(r'^edit_status/$', views.edit_status, name='edit_status'),
)

