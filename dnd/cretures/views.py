from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.



def cretures(req):
	'base model of all the living thing in game'
	cretures = models.Cretures.objects.get(id=1)
	return HttpResponse(f'{cretures}')

def adventurer(req):
	'player cherecter stat'
	return HttpResponse('adventurer')


def monster(req):
	'monster stat'
	return HttpResponse('monster')
