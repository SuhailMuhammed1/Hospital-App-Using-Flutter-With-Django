from django.conf.urls import url

from doctor import views
urlpatterns = [
    url('doc_reg/',views.docreg.as_view()),
    url('doclist/',views.doclist.as_view()),
    url('dcv/',views.dcv.as_view()),
    url('drpbook/',views.docdropbook.as_view()),
    url('vwpro/',views.vwprofile.as_view()),
    url('edit/',views.ed.as_view()),
    url('pr/',views.editpro.as_view()),
    url('deldoc/',views.deletedoc.as_view()),
    url('availdoc/',views.docavail.as_view())
]