from dataclasses import fields
from rest_framework import serializers

from .models import Campaigns, CampaignInfo, Projected_matrics

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns
        fields = '__all__'

class CampaignInfoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignInfo
        fields = ['campaign_name','campaign_status','campaign_desc','created_on','performance_ctr','performance_cvr']

class CampaignInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignInfo
        fields = '__all__'

class ProjectedMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projected_matrics
        fields = '__all__'

class CampaignInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignInfo
        fields = ['performance_ctr','performance_cvr']
