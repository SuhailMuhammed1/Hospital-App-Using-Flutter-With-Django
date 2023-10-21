from django.conf.urls import url

from lab import views
urlpatterns = [
    url('labreg/',views.labreg.as_view()),
    url('lablist/', views.lablt.as_view()),
    url('dellab/', views.dellab.as_view())
]