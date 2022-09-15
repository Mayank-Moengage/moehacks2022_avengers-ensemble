from django.http import JsonResponse
from django.shortcuts import render
from requests import request
from rest_framework.response import Response
from .models import Campaigns, CampaignInfo, Projected_matrics
from .serializers import CampaignSerializer,CampaignInfoGetSerializer,CampaignInfoSerializer, \
    ProjectedMetricsSerializer, CampaignInfoUpdateSerializer
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
@api_view(['GET'])
def index(req):
    campaign = Campaigns.objects.all()
    campiagnserial = CampaignSerializer(campaign, many=True)

    return Response(campiagnserial.data)
@api_view(['GET'])
def campaignView(req, pk):
    campaign = Campaigns.objects.get(name=pk)
    campiagnserial = CampaignSerializer(campaign, many=False)

    return Response(campiagnserial.data)

@api_view(['POST'])
def campaignAdd(req):
    serialdata = CampaignSerializer(data= req.data)
    if serialdata.is_valid():
        serialdata.save()

    return Response(serialdata.data)

@api_view(['POST'])
def campaignUpdate(req,pk):
    campaign = Campaigns.objects.get(id=pk)
    serialcampaign = CampaignSerializer(instance=campaign,data=req.data)

    if serialcampaign.is_valid():
        serialcampaign.save()
        return Response(serialcampaign.data)
    return Response("error")
    
@api_view(['DELETE'])
def campaignDelete(req,pk):
    campaign = Campaigns.objects.get(id=pk)
    campaign.delete()

    campaign = Campaigns.objects.all()
    campiagnserial = CampaignSerializer(campaign, many=True)

    return Response(campiagnserial.data)

@api_view(['GET'])
def campaignList(req):
    campaign = CampaignInfo.objects.all()
    campiagnserial = CampaignInfoGetSerializer(campaign, many=True)

    return Response(campiagnserial.data)

@api_view(['POST'])
def campaignRegister(req):
    serialdata = CampaignInfoSerializer(data= req.data)
    if serialdata.is_valid(raise_exception=True):
        serialdata.save()
    else:
        return Response({"result": "failed"}, status=status.HTTP_404_NOT_FOUND)
    return Response({"result": "created"}, status=status.HTTP_201_CREATED)


def update_values(cvr,ctr,user_percentage):
   campaign = CampaignInfo.objects.get(user_percentage=user_percentage)
   data_update = {'performance_cvr':cvr,'performance_ctr':ctr}
   serialcampaign = CampaignInfoUpdateSerializer(instance=campaign,data=data_update)
   if serialcampaign.is_valid(raise_exception=True):
        serialcampaign.save()

@api_view(['GET'])
def metricsList(req):
    projected_metrics = Projected_matrics.objects.all()
    projected_serial = ProjectedMetricsSerializer(projected_metrics, many=True)

    return Response(projected_serial.data)

@api_view(['POST'])
def metricsRegister(req):
    serialdata = ProjectedMetricsSerializer(data=req.data)

    if serialdata.is_valid(raise_exception=True):
        update_values(serialdata.validated_data.get('cvr'),serialdata.validated_data.get('ctr'),serialdata.validated_data.get('user_percentage'))
        serialdata.save()
    else:
        return Response({"result": "failed"}, status=status.HTTP_404_NOT_FOUND)
    return Response({"result": "created"}, status=status.HTTP_201_CREATED)

