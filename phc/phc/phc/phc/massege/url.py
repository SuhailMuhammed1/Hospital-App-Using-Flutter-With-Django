from django.conf.urls import url

from massege import views
urlpatterns = [
    url('msg/',views.msg.as_view()),
    url('vwmsg/', views.vwnmsg.as_view())
]