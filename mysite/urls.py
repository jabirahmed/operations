from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

runbook_patterns = patterns('',
	 url(r'^$', 'runbook.views.index'),
	 url(r'lookup/$', 'runbook.views.lookup'),
	 url(r'^alert/(?P<alert_id>\d+)/$', 'runbook.views.alert'),
	 url(r'^alert/$', 'runbook.views.alert',name='all_alerts'),
	 url(r'team/(?P<teamid>\d+)/$', 'runbook.views.teams',name="specific_team"),
	 url(r'teamMember/(?P<member_id>\d+)/$', 'runbook.views.team_member',name='team_member'),
	 url(r'teamMember/$', 'runbook.views.team_member',name='all_team_members'),
	 url(r'^team/$', 'runbook.views.teams',name='all_teams'),
	 url(r'^search/alert/$', 'runbook.views.search_alert',name='search_alert'),
	 url(r'^search/team/$', 'runbook.views.search_team_member',name='search_team_member'),
	 url(r'^oncallList/$', 'runbook.views.oncall_list',name='oncall_list'),
	 url(r'^runbooks/$', 'runbook.views.runbook_list',name='runbook_list'),
	 url(r'^runbooks/(?P<runbook_team_id>\d+)/$', 'runbook.views.runbook_list',name='runbooks_by_team'),
	 
)

urlpatterns = patterns('',
    url(r'^runbook/', include(runbook_patterns)),
    url(r'^polls/$', 'polls.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns+=staticfiles_urlpatterns()
