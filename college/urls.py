from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from college import views

urlpatterns = [
    url('^$', RedirectView.as_view(url='home/')),
    url('^home/$', views.home, name='home'),
    url('^student$', views.MyList.as_view(), name='student'),
    url('^notice/$', views.NoticeList.as_view(), name='nlist'),
    url('^notice/(?P<pk>[0-9]+)$', views.NoticeDetail.as_view(), name='ndet'),
    url('^assignment/$', views.AssignmentList.as_view(), name='alist'),
    url('^assignment/(?P<pk>[0-9]+)$', views.AssignmentDetail.as_view(), name='adet'),
    url('^result/$', views.ResultList.as_view(), name='rlist'),
    url('^result/(?P<pk>[0-9]+)$', views.ResultDetail.as_view(), name='rdet'),
    url('^attendance/$', views.AttendanceList.as_view(), name='atlist'),
    url('^attendance/(?P<pk>[0-9]+)$', views.AttendanceDetail.as_view(), name='atdet'),
    url(r'^edit_student/edit/(?P<pk>\d+)$', views.StudentUpdate.as_view(), name='student_edit'),
    url('^chkstu/', views.chkstu, name="chkstu"),
    url('^feedback/$', views.FeedCreate.as_view(), name='feed'),
    url('^submit_feedback/', views.SubmitFeedback, name='subFeed')
]
