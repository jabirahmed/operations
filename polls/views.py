# Create your views here.
from django.template import Context, loader
from polls.models import Poll
from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    return render_to_response("polls/index.html",{'latest_poll_list': latest_poll_list});
    t=loader.get_template("polls/index.html");
    c = Context({'latest_poll_list': latest_poll_list})
    res=HttpResponse(t.render(c))
    res.set_cookie("name","jabir")
    return res

def detail(request, poll_id):
    try:
	p=Poll.objects.get(pk=poll_id)
	import pdb;pdb.set_trace();
	n=request.get_signed_cookie("name")
    except Poll.DoesNotExist:
	raise Http404
    return render_to_response("polls/detail.html",{"poll":p,"na":n})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
