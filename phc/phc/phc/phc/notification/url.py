from django.conf.urls import url

from notification import views
urlpatterns = [
    url('noti/',views.notipost.as_view()),
    url('vntdr/',views.vwnotidr.as_view()),
    url('vwntpt/',views.vwnotipt.as_view()),
    url('vwntjhi/',views.vwnotijhi.as_view()),
    url('vwntlab/',views.vwnotilab.as_view()),
]