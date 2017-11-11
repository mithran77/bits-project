from django.conf.urls import url # pragma: no cover
from . import views # pragma: no cover

urlpatterns = [ # pragma: no cover
    url(r'^$', views.landing_page, name="landing_page"),
    #url(r'^paypal/', views.django_paypal, name="django_paypal"),
    url(r'^halls/$', views.hall_list, name="hall_list"),
    url(r'^caterers/$', views.caterer_list, name="caterer_list"),
    url(r'^florists/$', views.florist_list, name="florist_list"),
    url(r'^halls/(?P<pk>\d+)/$', views.hall_detail, name="hall_detail"),
    url(r'^caterers/(?P<pk>\d+)/$', views.caterer_detail, name="caterer_detail"),
    url(r'^florists/(?P<pk>\d+)/$', views.florist_detail, name="florist_detail"),
    url(r'^halls/(?P<pk>\d+)/bookdate$', views.bookdate_hall, name="bookdate_hall"),
    url(r'^caterers/(?P<pk>\d+)/bookdate$', views.bookdate_caterer, name="bookdate_caterer"),
    url(r'^florists/(?P<pk>\d+)/bookdate$', views.bookdate_florist, name="bookdate_florist"),
    url(r'^halls/[0-9]+/bookdate/(?P<pk>[0-9]+)/payment$', views.payment_hall, name="payment_hall"),
    url(r'^caterers/[0-9]+/bookdate/(?P<pk>[0-9]+)/payment$', views.payment_caterer, name="payment_caterer"),
    url(r'^florists/[0-9]+/bookdate/(?P<pk>[0-9]+)/payment$', views.payment_florist, name="payment_florist"),
]

