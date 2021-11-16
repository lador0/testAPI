from django.shortcuts import render
from django.http import HttpResponse
from first.models import data
import time

def api(request):
    method=request.GET['method']
    result=404
    if method=='save':
        date=request.GET['date']
        views=0
        clicks=0
        cost=0
        try:
            views=int(request.GET['views'])
        except:
            pass
        try:
            clicks=int(request.GET['clicks'])
        except:
            pass
        try:
            cost=float(request.GET['cost'])
        except:
            pass
        data.objects.create(date=date,views=views,clicks=clicks,cost=cost)
        result='Written'
        
    elif method=='view':
        from_loc=request.GET['from']
        to_loc=request.GET['to']
        
        got=data.objects.filter(date__lte=to_loc,date__gte=from_loc)
        result='<b>DATE====VIEWS====CLICKS====COST====CPC====CPM</b>'
        for i in got:
            result+='<p>'+str(i.date)+'===='+str(i.views)+'===='+str(i.clicks)+'===='+str(i.cost)+'===='+str(i.cost//i.clicks)+'===='+str(i.cost//(i.views*1000))+'</p>'
        
    elif method=='del':
        data.objects.all().delete()
        result='Deleted'
        
    return HttpResponse(result)







