from django.shortcuts import render, redirect
from .form import MyfileForm
from .models import MyfileUpload
from django.contrib import messages
import os

# Create your views here.
class Model:
    def home(request):
        mydata=MyfileUpload.objects.all()    
        myform=MyfileForm()
        if mydata!='':
            context={'form':myform,'mydata':mydata}
            return render(request,'index.html',context)
        else:
            context={'form':myform}
            return render(request,"index.html",context)
    
    def uploadfile(request):
        if request.method == 'POST':
            myform = MyfileForm(request.POST, request.FILES)
            if myform.is_valid():
                myFileName=request.POST.get('file_name')
                myFile1=request.POST.get('file')
                exists=MyfileUpload.objects.filter(my_file=myFile1).exists()

            if exists:
                messages.error(request,'The file %s is already exists...!!!'% myFile1)
            else:
                MyfileUpload.objects.create(file_name=myFileName,my_file=myFile1).save()
                messages.success(request,"File uploaded successfully.")
            return redirect("home")
        
    def deleteFile(request,id):
        mydata=MyfileUpload.objects.get(id=id)    
        mydata.delete()    
        os.remove(mydata.my_file.path)
        messages.success(request,'File deleted successfully.')  
        return redirect('home')
