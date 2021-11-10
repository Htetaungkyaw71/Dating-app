from django.http.response import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.db import IntegrityError, models
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from . models import Passion, User, Profile,SendMessage
from django.views.decorators.csrf import csrf_exempt
from .decorators import user_is_entry_author




            
def index(request):  
    p = []
    aa = []
    likes = []
    profiles = []
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()            
        messages = SendMessage.objects.filter(receiver=profile).all()
        smessages = SendMessage.objects.filter(sender=profile).all()     
        if profile: 
            profile.active = True  
            for bb in profile.liked.all():
                melikes = Profile.objects.filter(user=bb).all()  
                for ii in melikes:
                    likes.append(ii)  
            posts = Profile.objects.exclude(liked=request.user).all()         
            kk = Profile.objects.filter(liked=request.user).all()
            for jj in kk:
                profiles.append(jj)             
            loc = profile.location
            for post in posts: 
                if loc and post.location:
                    if loc <= post.location + 0.5 and loc >= post.location - 0.5:
                        p.append(post)   
                elif loc is None:
                    pp = Profile.objects.exclude(liked=request.user).all() 
                    return render(request,"pinner/index.html",{
                                    "posts":pp,
                                    "profile":profile,
                                    'passions':Passion.objects.all(),
                                    "male":"male",                   
                                    'count':0.5,
                                    "female":"female",                                 
                                })    
                elif post.location is None:
                    ppp = Profile.objects.exclude(liked=request.user,user=post.user).all() 
                    for i in ppp:
                        if loc <= i.location + 0.5 and loc >= i.location - 0.5:
                            aa.append(i)
                            return render(request,"pinner/index.html",{
                                            "posts":aa,
                                            "profile":profile,
                                            'passions':Passion.objects.all(),
                                            "male":"male",
                                            'count':0.5,
                                            "female":"female",
                                                
                                })    
                else:
                    pp = Profile.objects.exclude(liked=request.user).all() 
                    return render(request,"pinner/index.html",{
                                    "posts":pp,
                                    "profile":profile,
                                    'passions':Passion.objects.all(),
                                    "male":"male",                   
                                    'count':0.5,
                                    "female":"female",                                 
                                })                                      
        if not profile:
            return HttpResponseRedirect(reverse('create'))
        mm = []
        list1_as_set = set(likes)
        intersection = list1_as_set.intersection(profiles)
        intersection_as_list = list(intersection)
        return render(request,"pinner/index.html",{
            "posts":p,
            "profile":profile,
            'passions':Passion.objects.all(),
            "male":"male",  
            'count':0.5,
            "female":"female",
            "matches":intersection_as_list,
            "messages":messages,
            "smessages":smessages,
            "mm":SendMessage.objects.all(),
            "count":len(intersection_as_list)
        })
    else:
        return HttpResponseRedirect(reverse('login'))
    
def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["cpassword"]
        if password != confirm:
            return render(request,"pinner/register.html",{
                "message":"password didn't match"
            })
        try:
            user = User.objects.create_user(username,email,password)
            user.save()       
        except IntegrityError:
            return render(request,"pinner/register.html",{
                "message":"username is already taken"
            })
        login(request,user)
        return HttpResponseRedirect(reverse("home"))
    return render(request,"pinner/register.html")
    

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"] 
        password = request.POST["password"]

        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request,"pinner/login.html",{
                "message":"Invalid Credinals"
            })
    else:
        return render(request,"pinner/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@user_is_entry_author
@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        birth = request.POST["date"]
        gender = request.POST["gender"]
        like_gender = request.POST["like_gender"]
        interest = request.POST["interest"]
        height = request.POST["height"]
        images = request.FILES.get('image')
        new = Profile.objects.create(
            user=request.user,
            birth=birth,
            user_gender=gender,
            like_gender=like_gender,
            interest=interest,
            height=height,
            image = images,
            )
        for i in request.POST.getlist("passion"):
            passion = Passion.objects.get(id=i)
            new.passions.add(passion)
            new.save()          
        return HttpResponseRedirect(reverse('home'))
    return render(request,"pinner/create.html",{  
        "passions":Passion.objects.all()
    })




def delete(request,id):
    user = User.objects.get(id=id)
    if user == request.user:
        user.delete()
    else:
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(reverse('home'))


def edit(request,id):
    profile = Profile.objects.get(id=id)
    if request.method == "POST":      
        profile.user =request.user
        profile.birth = request.POST["birth"]
        profile.user_gender = request.POST["gender"]
        profile.like_gender = request.POST["like_gender"]
        profile.interest = request.POST["interest"]
        profile.height = request.POST["height"]
        i = request.FILES.get('image')
        if i is not None:
            profile.image = i
        passions = Passion.objects.all()
        for a in passions:
            profile.passions.remove(a) 
            profile.save()   
        for i in request.POST.getlist("passion"):
            passion = Passion.objects.get(id=i)
            profile.passions.add(passion) 
            profile.save()
        return HttpResponseRedirect(reverse('home'))
        
@csrf_exempt
def location(request,id):
    profile = Profile.objects.get(id=id)
    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("location") is not None:
            profile.location = data["location"]
        profile.save()
        return HttpResponse(status=204) 
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)  


def like(request,id):
    profile = Profile.objects.get(id=id)
    if request.method == "GET":
        if profile:
            profile.liked.add(request.user)
            profile.unliked.remove(request.user)
            profile.save()
            return HttpResponse(status=200)
    else:
        return JsonResponse({
            "error":"GET method required"
        },status=400)

def nope(request,id):
    profile = Profile.objects.get(id=id)
    if request.method == "GET":
        if profile:
            profile.unliked.add(request.user)
            profile.liked.remove(request.user)
            profile.save()
            return HttpResponse(status=200)
    else:
        return JsonResponse({
            "error":"GET method required"
        },status=400)

def message(request,id,message):
    receiver = Profile.objects.get(id=id)
    sender = Profile.objects.filter(user=request.user).first()
    if request.method == "GET":
        new = SendMessage.objects.create(sender=sender,message=message,receiver=receiver)
        new.save()
        return HttpResponse(status=200)
    else:
        return JsonResponse({
            "error":"GET method required"
        },status=400)


def pp(request,id):
    profile = Profile.objects.get(id=id)
    return render(request,"pinner/profile.html",{
    "profile":profile
    }  )


def unmatch(request,id):
    profile = Profile.objects.get(id=id)
    if request.method == "GET":
        if profile:
            profile.liked.remove(request.user)
            profile.unliked.add(request.user)          
            profile.save()
            return HttpResponse(status=200)
    else:
        return JsonResponse({
            "error":"GET method required"
        },status=400)






