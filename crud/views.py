from django.shortcuts import render,redirect
from .import views, messages
from .models import form1
def home(request):
    data=form1.objects.all()
    context={"data":data}
    
    return render(request,'home.html',context)

# Create your views here.
def add(request):
    data=form1.objects.all()
    context={"d":data}
    if request.method=="POST":
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        phone = request.POST.get('phone')
        query=form1(name='name',rollno='rollno',phone='phone')
        query.save()
        return redirect("/")
    return render(request,'home.html',context)

def update(request,id):
    if request.method=="POST":
        name=request.POST['name']
        rollno=request.POST['rollno']
        phone=request.POST['phone']
        edit=form1.objects.get(id=id)
        edit.name=name
        edit.rollno=rollno
        edit.phone=phone
       
        edit.save()
        return redirect("/")
    d=form1.objects.get(id=id) 
    context={"d":d}
    return render(request,"update.html",context)
def delete(request,id):
    d=form1.objects.get(id=id) 
    d.delete()
    
    return redirect("/")
    

    

  
       

