from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
import uuid
"""
    The above code defines views for a dashboard, upcoming tasks, completing tasks, and a 404 error page
    in a Django web application.
    
    :param request: The `request` parameter in Django views represents the HTTP request that was sent to
    the server. It contains information about the request, such as the user's browser details, any data
    sent in the request, and other metadata. The view function processes this request and returns an
    HTTP response, which is then
    :return: The views for the dashboard, upcoming tasks, completing tasks, and a 404 page are being
    returned in the Django views file. Each view renders a specific HTML template with context data
    containing an image, title, and other relevant information for the respective page.
"""
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import json
from .models import Todo,User_Model

# Create your views here.
def verify_user(request): 
    if request.method == 'POST':
        username=request.POST['name']
        password=request.POST['password']
        obj=User_Model.objects.filter(password=password,name=username)
        
        if len(obj) != 0:
           res=redirect('/dashboard/')
           res.set_cookie('id',obj[0].token_id)
           return res
        else:
            return redirect('/login/')
        
def delete_completed(request,id):
    if request.method == 'POST':
        obj=Todo.objects.get(todo_id=id)
        obj.delete()
        return redirect('/complete/')

def logout(request):
    if 'id' in request.COOKIES:
        res=redirect('/login/')
        res.delete_cookie('id')
        return res
    else:
        return redirect('/login/')


def add_user(request): 
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        hex_code = uuid.uuid4().hex[:6]
        url=f'https://dummyimage.com/600x400/{hex_code}/fff&text={username[:1]}'
        try:
            id=str(uuid.uuid4())
            obj=User_Model(name=username,email=email,password=password,token_id=id,avatar=url)
            obj.save()
            messages.success(request, "User is added succesfully")
            res=redirect('/dashboard/')
            res.set_cookie('id',id)
            return res
        except:
            messages.error(request, "User does not added successfully.")
            return redirect('/signup/')
        
def profile(request):
    if 'id' in request.COOKIES:
        user=User_Model.objects.filter(token_id=request.COOKIES['id'])
        return render(request,'profile.html',{"title":user[0].name,"user":user[0],"isprofile":True,"img":user[0].avatar,"alt":"image"})
    else:
        return redirect('/login/')
               
def mark_as_complete(request,id): 
    if request.method == 'POST':
        obj=Todo.objects.get(todo_id=id)
        obj.is_completed=True
        obj.save() 
        return redirect('/dashboard/')

def delete(request,id): 
    if request.method == 'POST':
        obj=Todo.objects.get(todo_id=id)
        obj.delete()
        return redirect('/dashboard/')

def edit(request,id): 
    if request.method == 'POST':
        obj=Todo.objects.get(todo_id=id)
        print(request.POST)
        obj.title=request.POST['title']
        obj.priority=request.POST['priority']
        obj.save() 
        return redirect('/dashboard/')

def edit_profile(request): 
    if request.method == 'POST':
        if 'id' in request.COOKIES:
            user=User_Model.objects.get(token_id=request.COOKIES['id'])
            user.name=request.POST['name']
            user.email=request.POST['email']
            user.avatar=request.POST['url']
            user.save() 
            return redirect('/profile/')
        else:
            return redirect('/login/')

def add_todo(request): 
    if request.method == 'POST':
        title=request.POST['title']
        user_id=request.POST['id']
        date=request.POST['date']
        time=request.POST['time']
        priority=request.POST['priority']
        print(user_id)
        try:
            obj=Todo(title=title,date=date,priority=priority,time=time,user_id=request.COOKIES['id'])
            obj.save()
            messages.success(request, "Todo is added succesfully")
            
        except:
            messages.error(request, "Todo does not added successfully.")
        print(request)
        return redirect('/dashboard/')

def login(request): 
    return render(request,'login.html')
def signup(request): 
    return render(request,'signup.html')
   
def dashboard(request):
    if 'id' in request.COOKIES:
        obj=Todo.objects.filter(user_id=request.COOKIES['id'],is_completed=False)
        user=User_Model.objects.filter(token_id=request.COOKIES['id'])
    # The above code is a Python script that defines a dictionary `context` containing various
    # key-value pairs. The dictionary includes keys such as 'id', 'img', 'alt', 'title', and
    # 'navigation'. The 'img' key contains a base64-encoded image data, while the 'navigation' key
    # contains a list of dictionaries with 'title' and 'priority' keys.
        context={
            'id':request.COOKIES['id'],
            "img":user[0].avatar,
            "alt":"image",
            "title":"Today's task",
            "navigation":obj,
            "isprofile":False
        }
        return render(request,'index.html',context)
    else:
        return render(request,'login.html')



def completing(request):
    if 'id' in request.COOKIES:
        obj=Todo.objects.filter(user_id=request.COOKIES['id'],is_completed=True)
        user=User_Model.objects.filter(token_id=request.COOKIES['id'])
        context={
            'id':request.COOKIES['id'],
            "img":user[0].avatar,
            "alt":"image",
            "title":"Complete task",
            "navigation":obj,
            "isprofile":False
        }
        return render(request,'complete.html',context)
    else:
        return render(request,'login.html')

def not_found(request):
    return render(request, "404.html", status=404)

