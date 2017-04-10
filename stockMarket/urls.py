from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from stocks import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stocks/$',views.StockList.as_view()),
    url(r'^stocks/create$',views.StockListCreate.as_view()),
    url(r'^stocks/(?P<pk>[0-9]+)/$',views.StockRetrieve.as_view()),
    url(r'^stocks/(?P<pk>[0-9]+)/edit$',views.StockRetrieveUpdate.as_view()),
    url(r'^stocks/(?P<pk>[0-9]+)/delete$',views.StockRetrieveDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
