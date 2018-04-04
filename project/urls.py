from django.conf.urls import include, url
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^chat/', include('chat.urls'), name='chat'),
    url(r'^.*$', RedirectView.as_view(pattern_name='index'))
]
