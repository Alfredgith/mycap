from django.shortcuts import render,redirect
from .models import wap,van
from .forms import mywap,myvan

def gas(request):
    form=myvan()
    if request.method=='POST':
       form=myvan(request.POST,request.FILES)
       if form.is_valid():
          form.save()
          return redirect('/gas')
          
       
    else:
        form=myvan()
        gas1=van.objects.all()
        return render(request,'index.html1',{'form':form,'gas1':gas1})
        
       
def has(request):
    has1=wap.objects.all()
    return render(request,'index.html2',{'has1':has1})
