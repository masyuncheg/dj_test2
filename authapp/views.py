from django.shortcuts import render
import MySQLdb
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .models import MyUser
from django.db import IntegrityError


@ensure_csrf_cookie
def log_view(request):
    if request.method=='POST':

        login1=request.POST.get('login')
        password=request.POST.get('password')

        if not login1:
            return JsonResponse({'error':'Заполните логин.'},status=400)

        if not password:
            return JsonResponse({'error':'Заполните пароль.'},status=400)
    
        user=authenticate(request,username=login1, password=password)

        if user is not None:
            login(request,user)
            return JsonResponse({'success':'Вы успешно авторизировались'})
        else: 
            return JsonResponse({'error':'Неверный логин или пароль'},status=400)
        
    if request.method=='GET':
        return render(request,'authapp/log.html')
    else:
        return JsonResponse({'error':'403'},status=403)
    
@ensure_csrf_cookie
def reg_view(request):
    if request.method=='POST':
        login=request.POST.get('login')
        password=request.POST.get('password')
        email=request.POST.get('mail')
        gender=request.POST.get('gender')

    
        if not login or not password or not email or not gender:
            return JsonResponse({'error':'Запоните все поля'},status=400)
        
        try:
            user=MyUser.objects.create_user(
                username=login,
                email=email,
                password=password,
                gender=gender
            )
        except IntegrityError as a:
            return JsonResponse({'error':'Такой логин уже существует'})
        
        return JsonResponse({'success':'Вы успешно зарегистрировались'})
       
    if request.method=='GET':
        return render(request, 'authapp/reg.html') 
    else:
        return JsonResponse({'error':'403'},status=403) 
            




        

    


