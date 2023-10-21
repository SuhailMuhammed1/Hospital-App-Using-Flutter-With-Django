from django.conf.urls import url

from pateint_lab_det import views
urlpatterns = [
    url('patlab/',views.labpat.as_view()),
    url('lab',views.lab.as_view()),
    url('vw/',views.view_labreport.as_view())

]