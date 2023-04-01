from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import customer,crud
from .forms import stuform,Addform
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.





def index(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        customer(firstname=firstname,lastname=lastname,email=email,username=username,password=password).save()

    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def stulog(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        stud=customer.objects.filter(username=username,password=password)
        if stud:
            user_details=customer.objects.get(username=username,password=password)
            id=user_details.id
            email= user_details.email
            username=user_details.username
            request.session['id']=id
            request.session['username']=username
            request.session['email']=email


            send_mail(
            'login message',
            'Hi '+username+ ', sussesfully login' ,
            'binualex92@gmail.com',
            [email],
            fail_silently=False,
)
            
            return redirect('welcome')
        else:
            return render(request,'login.html')
    else:
        return render(request,'index.html')
    
def welcome(request):
    id=request.session['id']
    username=request.session['username']
    return render(request,'welcome.html',{'id':id,'username':username})

def stuupdate(request,pk):
    cr=customer.objects.get(id=pk)
    form=stuform(instance=cr)
    if request.method=="POST":
        form=stuform(request.POST,instance=cr)
        if form.is_valid:
            form.save()
        redirect('welcome')   
    return render(request,"stuedit.html",{'form':form})



def imacreate(request):
    form = Addform()
    if request.method =="POST":
        form = Addform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect("welcome")
    return render(request,"ima.html",{'form':form})

def view(request):
    cr = crud.objects.all()
    return render(request,"view.html",{'cr':cr})
