from django.conf.urls import url

from health_inspector import views
urlpatterns = [
    url('hlt/',views.htreg.as_view()),
    url('jhilist/', views.jhilt.as_view()),
    url('deljhi/', views.delj.as_view())
]