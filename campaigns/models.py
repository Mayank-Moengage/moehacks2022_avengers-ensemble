from tkinter.tix import Tree
from django.db import models

# Create your models here.
class Campaigns(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class CampaignInfo(models.Model):
    campaign_name = models.CharField(max_length=50,unique=True, null=False)
    campaign_intent = models.CharField(max_length=50, null=False)
    campaign_desc = models.CharField(max_length=250)
    kpi_event = models.CharField(max_length=50, null=False)
    user_percentage = models.FloatField()
    performance_ctr = models.FloatField(default=0.0)
    performance_cvr = models.FloatField(default=0.0)
    campaign_status = models.CharField(max_length=50,default="Scheduled")
    created_on = models.DateTimeField(auto_now_add=True)

class Projected_matrics(models.Model):
    user_percentage = models.FloatField(default=0.0)
    ctr = models.FloatField(default=0.0)
    cvr = models.FloatField(default=0.0)