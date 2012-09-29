from django.contrib import admin
from runbook.models import *
from django import forms

class AlertModelForm(forms.ModelForm):
	desc = forms.CharField(widget=forms.Textarea)
	example= forms.CharField(widget=forms.Textarea)
	class Meta:
	 	model=Alert

class AlertAdmin(admin.ModelAdmin):
	search_fields = ['alert','desc']
	form=AlertModelForm

class RunBookAdmin(admin.ModelAdmin):
	search_fields=['runbook_url']
		
admin.site.register(Team)
admin.site.register(Runbook,RunBookAdmin)
admin.site.register(Alert,AlertAdmin)
admin.site.register(TeamMembers)
admin.site.register(Oncall)
