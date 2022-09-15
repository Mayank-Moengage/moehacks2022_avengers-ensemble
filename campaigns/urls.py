from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="/"),
    path("campaign-name/<str:pk>", views.campaignView, name="campaignview"),
    path("add-campaign", views.campaignAdd, name="campaignadd"),
    path("update-campaign/<str:pk>", views.campaignUpdate, name="campaignupdate"),
    path("delete-campaign/<str:pk>", views.campaignDelete, name="campaigndelete"),
    path("get_campaign_list",views.campaignList,name="campaignlist"),
    path("register_campaign",views.campaignRegister, name ="campaignregister"),
    path("register_metrics",views.metricsRegister, name="metricsregister"),
    path("get_metrics_list",views.metricsList,name="metricslist"),
]