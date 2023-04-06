from django.contrib import admin
from django.urls import path, re_path
from BlogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('^mail/', views.mail_send_view),

    # path('^tag/(?P<tag_slug>[-\w]+)/$', views.post_list_view, name='post_list_by_tag_name'),

    path('tag/<tag_slug>', views.post_list_view, name='post_list_by_tag_name'),

    path('<year>/<month>/<day>/<post>/', views.post_detail_view, name='post_detail'),

    path("<id>/share/", views.mail_send_view),

    # use-in-last
    re_path('^.*$', views.post_list_view),
    # re_path('^.*$', views.PostListView.as_view()),
]
