from django.conf.urls import url

from patient import views
urlpatterns = [
    url('patreg/',views.patreg.as_view()),
    url('patdrop/',views.patdrop.as_view()),
    url('patlist/',views.patlist.as_view()),
    url('patv/',views.edpropatient.as_view()),
    url('pated/',views.editpropat.as_view()),
    url('delpat/',views.deletepat.as_view())



]