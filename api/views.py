from django.shortcuts import render,HttpResponse
from .models import AllsafeWebsite
from django.views import View
import urllib3
from datetime import datetime
import json

def get_count(date,status):
    return AllsafeWebsite.objects.filter(date=date,status=status).count()
    

class AllSafeWebInfo(View):
    def get(self,request):
        today_date=datetime.now().date()
        return HttpResponse(json.dumps({"uptime":get_count(today_date,200),"downtime":get_count(today_date,500)}))
            

class HomePage(View):
    def get(self,request):
        return render(request,"html/home.html")

class GetDateWiseData(View):
    def get(self,request):
        today_date=datetime.now().date()
        date=request.GET.get("date",today_date)
        
        json_res={"uptime":get_count(date,200),"downtime":get_count(date,500)}
        return HttpResponse(json.dumps(json_res))
