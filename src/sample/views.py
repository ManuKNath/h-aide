from django.shortcuts import render,redirect
from .forms import loginForm,registerForm,add_details
from django.contrib.auth import get_user_model,authenticate,login
from user.models import Details


def home_page(request):
	return render(request,"home.html")

def login_page(request):
	myform = loginForm(request.POST or None) 
	context = {"form":myform}
	if myform.is_valid():
		username = myform.cleaned_data.get('username')
		password = myform.cleaned_data.get('password')
		print(myform.cleaned_data)
		user = authenticate(username=username,password=password)
		if not user==None:
			login(request,user)
			print(request.user.is_authenticated())
			return redirect(home_page)
		else:
			print("Login Failed")
			return render(request,"login.html",{"form":myform,"invalid":True})
	return render(request,"login.html",context)

User = get_user_model()
def register_page(request):
	regform = registerForm(request.POST or None)  
	context = {"form":regform}
	if regform.is_valid():
		username = regform.cleaned_data.get('username')
		password = regform.cleaned_data.get('password')
		email = regform.cleaned_data.get('email')
		newuser = User.objects.create_user(username,email,password)
		return redirect(home_page)
	return render(request,"register.html",context)

def details_page(request):
	detailform = add_details(request.POST or None)
	context ={"form" : detailform}		
	if detailform.is_valid():
		try:
			if Details.objects.get(user_id=request.user.username):
				return render(request,"add_details.html",{"form":detailform,"invalid":True})
		except Exception as e:
			first_name = detailform.cleaned_data.get('first_name')
			last_name = detailform.cleaned_data.get('last_name')
			address = detailform.cleaned_data.get('address')
			age = detailform.cleaned_data.get('age')
			aadhar_id = detailform.cleaned_data.get('aadhar_id')
			disablity = detailform.cleaned_data.get('disablity')
			category = detailform.cleaned_data.get('category')
			percentage_disabliity = detailform.cleaned_data.get('percentage_disabliity')
			ward = detailform.cleaned_data.get('ward')
			house = detailform.cleaned_data.get('house')
			village = detailform.cleaned_data.get('village')
			education = detailform.cleaned_data.get('education')
			job = detailform.cleaned_data.get('job')
			income = detailform.cleaned_data.get('income')
			user_id = request.user.username
			#Details.objects.raw("INSERT INTO user_details VALUES(first_name,last_name,address,age,aadhar_id,disablity,category,percentage_disabliity,ward,house,village,education,job,income)")
			Details.objects.create(fname=first_name,lname=last_name,address=address,age=age,aadhar_id=aadhar_id,disability=disablity,category=category,percentage_disabliity=percentage_disabliity,ward_number=ward,house_number=house,village=village,educational_qualification=education,job=job,income=income,user_id=user_id)
			return redirect(home_page)
		
	return render(request,"add_details.html",context)		