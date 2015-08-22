from django.conf.urls import patterns, include, url
from wildlife import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'targoviste_wildlife_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
)

