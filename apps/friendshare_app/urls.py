from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.render_homepage),
    url(r'^render_account_builder/$', views.render_account_builder),
    url(r'^build_account$', views.build_account),
    url(r'^render_display/(?P<x_id>\d+)$', views.render_display),
    url(r'^render_account_fixer/(?P<x_id>\d+)$', views.render_account_fixer),
    url(r'^fix_account/(?P<x_id>\d+)$', views.fix_account),
    url(r'^delete_user/(?P<x_id>\d+)$', views.delete_user),
]