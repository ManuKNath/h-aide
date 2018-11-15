from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Details,scheme,application
from sample.views import no_details,no_schemes
# Create your views here.

def details_view(request):
	username = request.user.username
	try:
		queryset = Details.objects.get(user_id=username)
		context = {"objects" : queryset }
	except Exception as e:
		return redirect(no_details)
	return render(request,"view_details.html",context)
	
def scheme_view(request):
	username = request.user.username
	try:
		for_category = Details.objects.get(user_id=username).category
		if for_category:
			queryset = scheme.objects.raw("SELECT * from user_scheme where for_category=%s",[for_category])
			context = {"schemes" : queryset }
			test = scheme.objects.filter(for_category=for_category)
			if test:
				print(test)
			else :
				context = {"value" : True }
				return render(request,"view_schemes.html",context)
		else:
			context = {"value" : True }
			return render(request,"view_schemes.html",context)			
	except Exception as e:
		context = {"value" : True }
		return render(request,"view_schemes.html",context)
		print(e)	
	return render(request,"view_schemes.html",context)			

#new
def review_request(request):
	try:
		queryset = scheme.objects.raw("SELECT * from user_application")
		print(queryset)
		context = {"applications" : queryset }
	except Exception as e:
		context = {"value" : True }
		return render(request,"admin_home.html",context)
		print(e)	
	return render(request,"request_page.html",context)


#new
def details_review(request, name):
	print(name)
	try:
		queryset = Details.objects.get(fname=name)
		context = {"objects" : queryset }
		print(queryset)
	except Exception as e:
		return redirect(no_details)
	return render(request,"review_details.html",context)

def scheme_view_admin(request):

	queryset = scheme.objects.raw("SELECT * from user_scheme")
	context = {"schemes" : queryset ,"page":True }
	if queryset:
		print(queryset)
	else :
		context = {"value" : True }
		return render(request,"view_schemes.html",context)			
	return render(request,"view_schemes.html",context)			

def request_reject(request,fname):
	print("worked1")
	try:
		application.objects.filter(fname=fname).delete()
	except Exception as e:
		print("worked")

	return redirect(review_request)	