from django.shortcuts import render,redirect
from . models import AdminLogin
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout 



# Create your views here.

def home(req):
  return render(req,'home.html')
 
def layout(req):
  return render(req,'layout.html')

def aboutus(req):
  return render(req,'aboutus.html')

def services(req):
  return render(req,'services.html')


# Project
def projects(req):
  return render(req,'projects.html')

#Registration of User
def register_view(req):
   if req.method == 'POST':
      form = UserCreationForm(req.POST)
      if form.is_valid():
         user = form.save()
         login(req,user)
         return redirect('dashboard')
   else:
      initial_data = {'username':'','password1':'','password2':""}
      form = UserCreationForm(initial=initial_data)
   return render(req,'register.html',{'form':form})

#login
def login_view(req):
   if req.method == 'POST':
      form = AuthenticationForm(req , data = req.POST)
      if form.is_valid():
         user = form.get_user()
         login(req,user)
         return redirect('dashboard')
   else:
      initial_data = {'username':'','password1':''}
      form = UserCreationForm(initial=initial_data)
   return render(req,'login.html',{'form':form})


#logout
def logout_view(req):
   logout(req)
   return redirect('login')

#Dashboard
def dashboard(req):
   pass

# register
def register(req):
  return render(req,'register.html')

def logcode(request):
   if request.method=="POST":
      usertype=request.POST['usertype']
      userid=request.POST['userid']
      password=request.POST['password']
      if usertype=="admin":
         try:
            user=AdminLogin.objects.get(userid=userid,password=password)
            if user is not None:
               request.session['adminid']=userid
               return redirect('adminapp:adminhome')
         except ObjectDoesNotExist:
            return render(request,'login.html',{'msg':'Invalid User'})
         
'''      elif usertype=="teacher":
         try:
            teacher=Teacher.objects.get(emailaddress=userid,password=password)
            if teacher is not None:
               request.session['teacherid']=userid
               return redirect('teacherapp:teacherhome')
         except ObjectDoesNotExist:
            return render(request,'login.html',{'msg':'Invalid User'})
      # Student Login 
      elif usertype=="student":
         try:
            student=Student.objects.get(emailaddress=userid,password=password)
            if student is not None:
               request.session['studentid']=userid
               return redirect('studentapp:studenthome')
         except ObjectDoesNotExist:
            return render(request,'login.html',{'msg':'Invalid User'})'''