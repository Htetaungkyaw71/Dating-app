from django.urls import path
from .import views

urlpatterns = [
    path("",views.index,name="home"),
    path("register/",views.register_view,name="register"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),    
    path("create/",views.create,name="create"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('edit/<int:id>',views.edit,name="edit"),      
    path('location/<int:id>',views.location,name="location"),
    path('like/<int:id>',views.like,name="like"),
    path('nope/<int:id>',views.nope,name="nope"),
    path('unmatch/<int:id>',views.unmatch,name="unmatch"),
    path('pp/<int:id>',views.pp,name="pp"),
    path('message/<int:id>/<str:message>',views.message,name="message"),
]
