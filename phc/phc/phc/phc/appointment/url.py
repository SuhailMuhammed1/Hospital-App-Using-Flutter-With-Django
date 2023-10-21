from django.conf.urls import url
from appointment import views
urlpatterns = [
    url('book/',views.bookappoint.as_view()),
    url('mngappoint/',views.manageappoint.as_view()),
    url('acpt/',views.accept.as_view()),
    url('rej/',views.reject.as_view()),
    url('vappoint/',views.viewappoint.as_view())


]