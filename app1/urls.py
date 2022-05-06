from django.urls import path 



from . import views





urlpatterns = [
    
    path('', views.home, name="home"),
    path('second',views.second, name="second"),
    path('apps',views.apps ,name="apps"),
    path('gaming',views.gaming,name="gaming"),
    path('tech',views.tech,name="tech"),
    path('linux',views.linux,name="linux"),
    path('internet',views.internet,name="internet"),
    path('pasword',views.pasword,name="pasword"),
    path('stic',views.stic,name="stic"),
    path('update',views.update,name="update"),
    path('samsung',views.samsung,name="samsung"),
    path('what',views.what,name="what"),
    path('facebook',views.facebook,name="facebook"),
    path('spotify',views.spotify,name="spotify"),
    path('callduty',views.callduty,name="callduty"),
    path('punk',views.punk,name="punk"),  
    #path('stream', streamPageView.as_view(), name="stream"),
    path('insta',views.insta,name="insta"),
    path('phone',views.phone,name="phone"),
    path('w11',views.w11,name="w11"),
    path('game',views.game,name="game"),
    path('p50',views.p50,name="p50"),
    path('callcenter',views.callcenter,name="callcenter"),
    path('blog', views.PostList.as_view(), name="index"),
  path('<slug:slug>/', views.PostList.as_view(), name="post_detail"),
  
  #path("", views.home, name="home"),
  #path("contact", views.contact, name="contact"),
    

    

    


]
