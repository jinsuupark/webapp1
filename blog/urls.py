from django.urls import path,re_path
from blog.views import *

app_name = 'blog'

urlpatterns =[
    # Example: /blog/post
    path('',PostLV.as_view(),name='index'),
    path('post/',PostLV.as_view(),name='index'),
    # Example: /blog/post/kasjjndfkansfndaflkn
    re_path(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='detail'),

    # Example: /blog/archive
    path('archive/', PostAV.as_view(),name='post_archive'),
    # Example : /blog/archive/2019
    path('archive/<int:year>',PostYAV.as_view(),name='post_year_archive'),
    # Example : /blog/archive/2019/nov
    path('archive/<int:year>/<str:month>',PostMAV.as_view(),name='post_month_archive'),
    # Example : /blog/archive/2019/nov/10
    path('archive/<int:year>/<str:month>/<int:day>',PostDAV.as_view(),name = 'post_day_archive'),
    # Example : /blog/archive/today
    path('archive/today/',PostTAV.as_view(),name= 'post_today_archive'),


    # Example : /blog/tag
    path('tag/',TagCloudTV.as_view(),name='tag_cloud'),
    # Example : /bog/tag/tagname/
    path('tag/<str:tag>/',TaggedObjectLV.as_view(),name='tagged_object_list'),

    path('search/', SearchFormView.as_view(), name='search'),

    # Example : /blog/add
    path('add/',PostCV.as_view(),name='add'),
    # Example : /blog/99/update
    path('<int:pk>/update/',PostUV.as_view(),name='update'),
    # Example : /blog/99/delete
    path('<int:pk>/delete/',PostDeleteV.as_view(),name='delete'),

    #다운로드
    path('download/<int:id>',download,name='download'),
]
