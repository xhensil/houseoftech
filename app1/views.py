from django.db.models.fields import EmailField
from django.shortcuts import render
from.models import Post
from.models import Contact
from django.http import HttpResponse

from django.views import generic


# Create your views here.
def home(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name=name 
        contact.email=email 
        contact.message=message
        contact.save()
        return HttpResponse("<h1>THANK YOU </h1>")

        

    return render(request,'home.html' )

def about(request,id):
    
    return render(request, 'about.html')

def second(request):
    
    return render(request,'second.html')
def apps(request):
    
    return render(request,'apps.html')
def gaming(request):
    
    return render(request,'gaming.html')
def tech(request):
    
    return render(request,'tech.html')
def linux(request):
    
    return render(request,'linux.html')
def internet(request):
    
    return render(request,'internet.html')
def pasword(request):
    
    return render(request,'pasword.html')
def stic(request):
    
    return render(request,'stic.html')
def update(request):
    
    return render(request,'update.html')
def samsung(request):
    
    return render(request,'samsung.html')
def what(request):
    
    return render(request,'what.html')
def facebook(request):
    
    return render(request,'facebook.html')
def spotify(request):
    
    return render(request,'spotify.html')
def callduty(request):
    
    return render(request,'callduty.html')
def punk(request):
    
    return render(request,'punk.html')

   
def insta(request):
    
    return render(request,'insta.html')
def phone(request):
    
    return render(request,'phone.html')
def w11(request):
    
    return render(request,'w11.html')
def game(request):
    
    return render(request,'game.html')
def p50(request):
    
    return render(request,'p50.html')
def callcenter(request):
    
    return render(request,'callcenter.html')


class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html'


class DetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'





#class streamPageView(ListView):
  #  model = Streams
   # template_name = 'stream.html'

#def homepage(request):
#	return render(request, "home.html")

#def contact(request):
	#if request.method == 'Post':
		#form = ContactForm(request.POST)
		#if form.is_valid():
			#subject = "Website Inquiry" 
			#body = {
			#'first_name': form.cleaned_data['first_name'], 
			#'last_name': form.cleaned_data['last_name'], 
			#'email': form.cleaned_data['email_address'], 
			#'message':form.cleaned_data['message'], 
			#}
			#message = "\n".join(body.values())

			#try:
				#send_mail(subject, message, 'xhensilferhati@gmail.com', ['xhensilferhati@gmail.com']) 
			#except BadHeaderError:
				#return HttpResponse('Invalid header found.')
			#return redirect ("home.html")
      
	#form = ContactForm()
	#return render(request, "contact.html", {'form':form})
