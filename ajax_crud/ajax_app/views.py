from django.shortcuts import render
from django.http import JsonResponse
from .forms import StudentForm, User
from rest_framework import status


def home(request):
    form = StudentForm()
    obj = User.objects.all()
    context = {"form":form, "obj":obj} 
    return render(request, 'ajax_app\home.html', context)

def student_view(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            sid=request.POST.get('stuid')
            print(sid)
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            if sid :
                user = User(id=sid, name=name, email=email, password=password)
                user.save()
                return JsonResponse({"msg":"successfully updated"},status=status.HTTP_201_CREATED)
            else:
                user = User(name=name, email=email, password=password)
                user.save()
                return JsonResponse({"msg":"successfully created"},status=status.HTTP_201_CREATED)
                
        else:
            return JsonResponse({"msg":"invalid data"},status=status.HTTP_400_BAD_REQUEST)

def student_retrive_view(request):
    obj = User.objects.values()
    data = list(obj)
    return JsonResponse({"data":data},status=status.HTTP_200_OK)

def student_sp_retrieve(request):
    pk = request.GET.get("sid")
    obj = User.objects.get(id=pk)
    student_data = {"id":obj.id, "name":obj.name, "email":obj.email, "password":obj.password}
    return JsonResponse({"data":student_data},status=status.HTTP_200_OK)


def student_delete_view(request):
    pk = request.POST.get("sid")
    obj = User.objects.get(id=pk)
    obj.delete()
    return JsonResponse({"msg":"successfully deleted.."},status=status.HTTP_200_OK)

       
