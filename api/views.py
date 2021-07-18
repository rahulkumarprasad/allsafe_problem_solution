from django.shortcuts import render,HttpResponse
from .models import AllsafeWebsite
from django.views import View
import urllib3
from datetime import datetime
import json

class AllSafeWebInfo(View):
    def get(self,request):
        today_date=datetime.now().date()
        http = urllib3.PoolManager()
        url=request.GET.get("url","https://allsafe.in/")
        res = http.request('GET', url)
        status=res.status
        json_resp={"uptime":0,"downtime":0,"url":url}
        if status == 200 or status == 500:
            get_old_record=AllsafeWebsite.objects.filter(date=today_date,status=status)
            if len(get_old_record) == 0:
                AllsafeWebsite(status=status,total_request=1).save()
                get_old_record=AllsafeWebsite.objects.filter(status=status,total_request=1)

            else:
                get_old_record[0].total_request=int(get_old_record[0].total_request)+int(1)
                get_old_record[0].save()
                
            
            if get_old_record[0].status == 200:
                json_resp["uptime"]=get_old_record[0].total_request
                json_resp["downtime"]=AllsafeWebsite.objects.filter(date=today_date,status=500)
                if len(json_resp["downtime"])==0:
                    json_resp["downtime"]=0
                else:
                    json_resp["downtime"]=json_resp["downtime"][0].total_request

            else:
                json_resp["downtime"]=get_old_record[0].total_request
                json_resp["uptime"]=AllsafeWebsite.objects.filter(date=today_date,status=200)
                if len(json_resp["uptime"]) == 0:
                    json_resp["uptime"]=0
                else:
                    json_resp["uptime"]=json_resp["uptime"][0].total_request

        return HttpResponse(json.dumps(json_resp))

class HomePage(View):
    def get(self,request):
        return render(request,"html/home.html")

class GetDateWiseData(View):
    def get(self,request):
        today_date=datetime.now().date()
        date=request.GET.get("date",today_date)
        obj=AllsafeWebsite.objects.filter(date=date)
        uptime=obj.filter(status=200)
        downtime=obj.filter(status=500)
        json_res={"uptime":(uptime[0].total_request if len(uptime) != 0 else 0),"downtime":(downtime[0].total_request if len(downtime) !=0 else 0)}
        return HttpResponse(json.dumps(json_res))

class Temp(View):
    #build for giving 500 error
    def get(self,request):
        test=Stu.objects.all()
        return HttpResponse("asd")