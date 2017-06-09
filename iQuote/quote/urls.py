from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	#============== ROOT API ENDPOINT ==========================
	url(r'^$', views.api_root, name='root'),
	
	#============== ROUTES FOR QUOTES ==========================

	url(r'^quotes/$', views.QuoteList.as_view(), name='quote-list'),
	url(r'quotes/(?P<pk>[0-9]+)/$', views.QuoteDetail.as_view(), name='quote-detail'),

]

urlpatterns += format_suffix_patterns(urlpatterns)