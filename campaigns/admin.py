from django.contrib import admin

# Register your models here.
from .models import Campaigns, CampaignInfo, Projected_matrics
admin.site.register(Campaigns)
admin.site.register(CampaignInfo)
admin.site.register(Projected_matrics)