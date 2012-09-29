from django.db import models
from datetime import datetime

# Create your models here.
TEAMS_TYPE = (
    (0, 'Operations'),
    (1, 'Development'),
    (2, 'Others'),
)

class Team(models.Model):
	team_name=models.CharField(max_length=50);
	team_manager=models.CharField(max_length=50)
	team_email=models.EmailField(max_length=100)
	team_type=models.IntegerField(max_length=2,choices=TEAMS_TYPE,blank=True)
	def __unicode__(self):
		return self.team_name
	
class TeamMembers(models.Model):
	team=models.ForeignKey(Team)
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50,blank=True)
	designation=models.CharField(max_length=10,blank=True)
	skypeid=models.CharField(max_length=50)
	emailid=models.EmailField(max_length=50)
	mobile=models.CharField(max_length=50)
	landline=models.CharField(max_length=50,blank=True)
	def full_name(self):
		return self.first_name+" "+self.last_name
	def __unicode__(self):
		return self.first_name+" "+self.last_name +" ["+self.team.team_name+"]"
	
class Alert(models.Model):
	alert= models.CharField(max_length=150)
	desc= models.CharField(max_length=5000)
	example= models.CharField(max_length=5000,blank=True)
	priority=models.IntegerField()
	ttr=models.IntegerField(blank=True)
	opsteam=models.ForeignKey(Team,related_name="ops")
	dev_team=models.ForeignKey(Team,related_name="dev")
	dt_modified= models.DateTimeField(default=datetime.now)
	def __unicode__(self):
		return self.alert + " ["+self.opsteam.team_name+"/"+self.dev_team.team_name +"]"
	

class Runbook(models.Model):
	team=models.ForeignKey(Team)
	runbook_desc=models.CharField(max_length=100)
	runbook_url=models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.runbook_desc+ " [ "+self.team.team_name+" ]"
	
MAYBECHOICE = (
    (0, 'Primary'),
    (1, 'Secondary'),
    (2, 'Shadowing'),
)


class Oncall(models.Model):
	team=models.ForeignKey(Team)
	oncall=models.ForeignKey(TeamMembers)
	oncall_type=models.IntegerField(max_length=1, choices=MAYBECHOICE)
	start_date= models.DateTimeField()
	end_date= models.DateTimeField()
	
	def __unicode__(self):
		return self.team.team_name + " [ "+ self.oncall.full_name() +" ] "
	
