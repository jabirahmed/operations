# Create your views here.
from django.db.models import Q
from django.http import HttpResponse ,Http404
from django.template import Context,loader
from django.shortcuts import render_to_response,redirect
from runbook.models import *
from datetime import *
from django.contrib.auth.models import *
from django.template import RequestContext
from urllib2 import HTTPRedirectHandler
from django.contrib.redirects.models import *
from django.contrib.auth.decorators import login_required
import logging


logger = logging.getLogger(__name__)
#@login_required(login_url='/admin/?next=/runbook') 
def index(request):
	a=1
	
	t=loader.get_template("runbook/index.html")	
	c=RequestContext(request,{'a':"a"});	
	res=HttpResponse(t.render(c));
	return res;

def lookup(request):
	all_alerts=Alert.objects.all();
	t=loader.get_template("runbook/alertList.html")
	c=RequestContext(request,{'alerts':all_alerts})
	res=HttpResponse(t.render(c))
        return res

def alert(request,alert_id=None):
	try:
		opsoncall=[]
		devoncall=[]
		if(alert_id!=None): 
			alertInfo=Alert.objects.get(pk=alert_id)
			all=0
			oncall_list=Oncall.objects.filter(start_date__lte=datetime.now(),end_date__gte=datetime.now())
			opsteamid=alertInfo.opsteam.id
			devteamid=alertInfo.dev_team.id
			opsoncall=oncall_list.filter(team=opsteamid);
			devoncall=oncall_list.filter(team=devteamid);
			#import pdb; pdb.set_trace();
		else:
			alertInfo=Alert.objects.all().order_by("alert")
			all=1
	except Alert.DoesNotExist:
		raise Http404
	#import pdb; pdb.set_trace();
	return render_to_response("runbook/alertInfo.html",{"alert":alertInfo,"all":all,"opsoncall":opsoncall,"devoncall":devoncall},context_instance=RequestContext(request))
	
def search_alert(request):
	try:
		query = request.GET.get('alert_text', '');
		if query:
				qset=(
						Q(alert__icontains=query)|Q(example__icontains=query)|Q(desc__icontains=query)
					)
				alertInfo=Alert.objects.filter(qset)
				all=1
		#import pdb; pdb.set_trace();
		else:
				alertInfo=[]
				all=-1
	except Alert.DoesNotExist:
		raise Http404
	return render_to_response("runbook/alertInfo.html",{"alert":alertInfo,"all":all},context_instance=RequestContext(request))
		
def search_team_member(request):
	try:
		query = request.GET.get('geek_name', '');
		if query:
				qset=(
						Q(first_name__icontains=query)|
						Q(last_name__icontains=query)
					)
				teamInfo=TeamMembers.objects.filter(qset)
				#import pdb; pdb.set_trace();
				all=0
		#import pdb; pdb.set_trace();
		else:
				#import pdb; pdb.set_trace();
				teamInfo=[]
				all=0
	except Alert.DoesNotExist:
		raise Http404
	return render_to_response("runbook/teamInfo.html",{"team":teamInfo,"team_name":all},context_instance=RequestContext(request))
		
def team_member(request,member_id=None):
	try:
		if (member_id!=None):
			teamInfo=TeamMembers.objects.filter(id=member_id).order_by("first_name");
			teamName=0;
		else:
			teamInfo=TeamMembers.objects.all().order_by("first_name");
		#	teamName=Team.objects.get(id=team_id);
			teamName=0;
	except TeamMembers.DoesNotExist:
		raise Http404
		
#	import pdb; pdb.set_trace();
	return render_to_response("runbook/teamInfo.html",{"team":teamInfo,"team_name":teamName},context_instance=RequestContext(request))
	
def teams(request,teamid=None):
	
	if (teamid!=None):
		try:
			members=1
			teamInfo=TeamMembers.objects.filter(team_id=teamid);
			#import pdb; pdb.set_trace();
		except TeamMembers.DoesNotExist:
				raise Http404
	else:
		try:
			teamInfo=Team.objects.all().order_by("team_name");
			members=0
		except Team.DoesNotExist:
			raise Http404

	return render_to_response("runbook/teamList.html",{"team":teamInfo,"members":members},context_instance=RequestContext(request))
	
def oncall_list(request):
		try:
			
			oncall_list=Oncall.objects.filter(start_date__lte=datetime.now(),end_date__gte=datetime.now());
			
		except Oncall.DoesNotExist:
			raise Http404
		#import pdb; pdb.set_trace()
		return render_to_response("runbook/oncallList.html",{"oncall":oncall_list},context_instance=RequestContext(request))

def runbook_list(request,runbook_team_id=None):
	try:
		if runbook_team_id == None:
			runbooks=Runbook.objects.all().order_by("team","runbook_desc")
		else:
			runbooks=Runbook.objects.filter(team=runbook_team_id)
		
	
	except Runbook.DoesNotExist:
		raise Http404
	return render_to_response("runbook/runbookList.html",{"runbooks":runbooks},context_instance=RequestContext(request))