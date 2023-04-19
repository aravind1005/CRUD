from django.shortcuts import render, redirect

from .form import CrudForm

from .models import Employee

# Create your views here.

class Crud:
    def create(request):
        if request.method == "POST":
            form = CrudForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("create")
        else:
            form = CrudForm()
        context = {"form":form}
        return render(request, 'create.html', context)
    
    def readall(request):
        exist = Employee.objects.all()
        if exist == "":
            return render("Employee not found")
        return render(request, 'emp.html', {"data":exist})
    
    def read(request, id):
        exist = Employee.objects.filter(id = id).first()
        print(exist)
        if exist is not None:
            return render(request, 'read.html', {"data":exist})
        return render(request, 'read.html', {"data":False})
    
    def update(request, id):
        exist = Employee.objects.filter(id = id).first()
        if request.method == "POST":
            if exist is None:
                return render(request, 'update.html', {"data":False})
            else:
                form = CrudForm(request.POST, instance=exist)
                if form.is_valid():
                    form.save()
                    return redirect("create")
        else:
            form = CrudForm()
        context = {"form":form, "data":exist}
        return render(request, 'update.html', context)
    
    def delete(request, id):
        exist = Employee.objects.filter(id = id).first()
        if exist is None:
            return render(request, 'delete.html', {"data":False})
        else:
            exist.delete()
            context = {"data":exist}
        return render(request, 'delete.html', context)
