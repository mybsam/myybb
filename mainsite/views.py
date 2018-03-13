from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Message
from datetime import datetime
from django.template.loader import get_template
import json
from django import forms
# Create your views here.

def homepage(request):
  template=get_template('index.html')
  html=template.render() 
  return HttpResponse(html)

def passage(request,slug):
	template=get_template('passage.html')
	posts=Post.objects.all()
	article=Post.objects.get(slug=slug)
	html=template.render(locals())
	return HttpResponse(html)

class MessageForm(forms.Form):
	name=forms.CharField(required=True)
	words=forms.CharField(required=True)


def message(request):
	try:
		obj=MessageForm(request.POST)
		ret=obj.is_valid()
		if ret:
			na=request.POST['name']
			wo=request.POST['words']
			ad=request.POST['address']
			p=Message.objects.create(name=na,words=wo,address=ad)
			p.save()
			res={"msg":"留言成功"}
			return HttpResponse(json.dumps(res))		
	except:
		res={"msg":"留言成功"}
		return HttpResponse(json.dumps(res))
	
	
	
		