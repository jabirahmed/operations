# Create your views here.
from django.http import HttpResponse
from django.template import Context,loader
from django.shortcuts import render_to_response
from runbook.models import *

def index(request):
	t=loader.get_template("runbook/lookup.html")	
	c=Context();	
	res=HttpResponse(t.render(c));
	return res;

def lookup(request):
	all_alerts=Alert.objects.all();
	t=loader.get_template("runbook/alertList.html")
	c=Context({'alerts':all_alerts})
	res=HttpResponse(t.render(c))
        return res

def alert(request,alert_id):
	try:
		alertInfo=Alert.objects.get(pk=alert_id)	
	except Alert.DoesNotExist:
		raise Http404
	return render_to_response("runbook/alertInfo.html",{"alert":alertInfo})
	
	
	
