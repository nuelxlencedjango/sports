#from django.views.generic import View

from django.shortcuts import render ,redirect ,get_object_or_404
from django.views.generic.base import TemplateView

from django.views.generic import (
    ListView ,DetailView, CreateView, UpdateView ,DeleteView
)
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from .models import *
from .forms import * #PlayersForms # PlayerRegisterForm
from django.http import Http404

from django.contrib import messages
from django.db.models import Q 

# email setting
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.

#from django.conf import settings
#from django.contrib import messages
#from django.core.exceptions import ObjectDoesNotExist
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin

#from django.views.generic import ListView ,DetailView ,View 
#from .forms import checkoutForm ,CouponForm,RefundForm,PaymentForm
#from django.views.generic.detail import  DetailView
#from django.views.generic import  View
#from django.shortcuts import redirect
#from django.utils import timezone
#from .forms import CheckoutForm
# , CouponForm, RefundForm, PaymentForm
#from .models import Item, OrderItem ,Order,Address,Payment ,Coupon,Refund,UserProfile
#import random
#import string
#import stripe

#from django.shortcuts import render
#from .models import *
#from django.http import JsonResponse
#import json
#import datetime
#from .utility import *

#context ={
 #   'posting' : News.objects.all(),
  #  'posts' : Post.objects.all(),
  #  'training' :Training.objects.all()

#}
    
#def news(request):
 #   newspost = Ne.objects.raw("select max(salary) from emp")
  #   "select empid,empname,salary from emp order by salary desc limit 1"
   # "select empid,empname,salary from emp order by salary asc limit 2"
    #"select empid,empname,salary from emp e1 where '+salary+'=(select count(distinct salary) from emp e2 where e1.salary>=e2.salary"
  
  #  return render(request ,'home.html' ,{'posting' : newspost }) 

#def recieveMail(request):
 #   if request.method ==' POST':
  #      message = request.POST['message']
   #     send_mail('conctact form' ,message ,settings.EMAIL_HOST_USER,
    #    ['nuel4xelence@gmail.com'],
     #   fail_silently=False)

   # return render (request ,'contacts.html')    



class NewsListView(ListView):
    #model = Post # model name
    #queryset = News.objects.all()
    template_name = ".html"  # template name/path
    context_object_name ="post" # context properties
    ordering =['-date_posted']   # arraned according date posted
    paginate_by =5



class TrainListView(ListView):
    model = Training # model name
    template_name = 'training.html'  # template name/path
    context_object_name ='training' # context properties
    ordering =['-date_posted']   # arraned according date posted
    #paginate_by =5
   # fetching posts from a particular poster

class UserPostListView(ListView):
    model = Post # model name
    template_name = 'user_posts.html'  # template name/path
    context_object_name ='posts' # context properties
    ordering =['-date_posted']   # arraned according date posted

    #pagination
    paginate_by =5

    # getting queryset from the db
    def get_queryset(self):
        user = get_object_or_404(User ,username =self.kwargs.get('username')) # getting the username ,if not ,return 404
        return Post.objects.filter(author = user).order_by('-date_posted')  # arraned according date posted


class PostDetailView(DetailView):
    model = News
    template_name = 'details.html' 
   
    
 
class NewsDetailView(DetailView):
    model = Post
    template_name = 'details.html' 
#def post_detail(request,id):
    #obj = get_object_or_404(Post ,id=id)
    #return render(request ,'post_detail.html' ,{'obj' :obj})


# creating a post class
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    fields =['title' ,'content']
    template_name = 'post_form.html' 

    # creating instance of user to make a post
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_invalid(form) # come back


# creating a post class
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    fields =['title' ,'content']
    template_name = 'post_form.html' 

    # creating instance of user to make a post
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_invalid(form)



def registration(request): 
    if request.method == 'POST':
        form = PlayersForms(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            print('successful')
            # Get the current instance object to display in the template
            img_obj = form.instance
            return redirect('info:home')
        else:
            print('invalid form')    
    else:
        form = PlayersForms()
        print('invlid form')
    return render(request, 'register.html', {'form': form})







    #if request.method == "GET":
       # form = PlayersForms()
       # return render(request ,'register.html' ,{'form':form})

    #else:
       # form = PlayersForms(request.POST)
       # print(form)
       # if form.is_valid():
            #print(form.firstname.data)
           # form.save()
         
        #else:
         #   print('invlad data')

        #return redirect('info:home')
    

#def index(request):
 #   form = CustomerForm()

  #  if request.method =='POST':
   #     form =CustomerForm(request.POST)
    ##       form.save()

    #context = {'form':form}
    #return render(request ,'customer.html',context)



#def register(request):
 ##      form = PlayersForm()
   #     return render(request ,'register.html' ,{'form':form})

    #else:

     #   form = PlayersForm(request.POST)
      #  if form.is_valid():
       #     form.save()
        #return redirect('news:home')

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = '/'
    #template_name = 'post_detail.html' 

    #authenticating the author of the post
    def test_func(self):
        post = self.get_object() # object -current user
        if self.request.user == post.author: # author of the post
            return True
        return False    

def about(request):

    return render(request ,'about.html')


def mission(request):
    return render(request ,'mission.html')

def training(request):

    return render(request ,'training.html')


#def matches(request):
  #  up_matches = ImportantMatches.objects.all()
    
  #  return render(request ,'matches.html' ,
  #  {'upComingMatches' : up_matches} )

 
     





class PostListView(TemplateView):
    template_name = 'home.html' 
    ordering =['-date_posted']   
     
    def get_context_data(self ,**kwargs):
        context = super().get_context_data(**kwargs)

        context['post'] = Post.objects.all()
        context['train'] = News.objects.all()
        context['coach'] = Coach.objects.all()
      

        return context

    #pagination
    paginate_by =5




class PlayersView(ListView):
    model = PlayersRegistration # model name
    template_name = 'players.html'  # template name/path
    context_object_name ='footballers' # context properties
    #ordering =['-date_posted']   # arraned according date posted




def search(request):
    query = request.GET.get('search' ,'')
    reg = PlayersRegistration.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
    if reg:

        messages.success(request ,"success")
        return render(request ,'search.html' ,{'reg' :reg})
    else:
        return redirect('info:players_info') 
        messages.success(request ,"no player like that")  




class MatchView(TemplateView):
    #model = ImportantMatches # model name
    template_name = 'matches.html'  # template name/path


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['upComingMatches'] =ImportantMatches.objects.all()
        context['italy'] =ItalianSerieA.objects.order_by('-point' ,'-goalf')
        context['england'] =Premiership.objects.order_by('-point' ,'-goalf')
        context['spain'] =Laliga.objects.order_by('-point' ,'-goalf')
        context['germany'] =Bundesliga.objects.order_by('-point' ,'-goalf')
        context['france'] =Ligue1.objects.order_by('-point' ,'-goalf')
        #context['turkey'] =Turkey.objects.order_by('-point' ,'-goalf')
        #context['prem'] =PremierS.objects.order_by('-point' ,'-goalf')
        return context

    #pagination
    #paginate_by =5
        
    #ordering =['-date_posted']   # arraned according date posted
    #paginate_by =5


#not useful
def insert_english(request):
    english = Premiership.objects.all()
    contex ={
        'english' : english,
        'league' : premiership
    }
    return render(request ,'match.html' ,contex)


def insert_spain(request):
    spainish = Laliga.objects.all()
    contex ={
        'spain' : laliga,
        'league' : spanish
    }
    return render(request ,'match.html' ,contex)


def insert_france(request):
    french = Ligue1.objects.all()
    contex ={
        'france' : french,
        'league' : french
    }
    return render(request ,'match.html' ,contex)  


def insert_germany(request):
    germany = Bundesliga.objects.all()
    contex ={
        'germany' : germany,
        'league' : german
    }
    return render(request ,'match.html' ,contex)  


def insert_italy(request):
    italy = SerieA.objects.all()
    contex ={
        'italy' : italy,
        'league' : seriea
    }
    return render(request ,'match.html' ,contex)   


def add_team(request ,cls):
    if request.method == 'POST':
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info:matches')
        else:
            print('invalid form')
    else:
        form = cls()
        return render(request ,'create.html' ,{'form' :form})            

# end here

#def add_english(request):
 #   return add_team(request ,PremiershipForm)


###def add_german(request):
   # return add_team(request ,BundesligaForm)

#def add_italian(request):
 #   return add_team(request ,ItalianSerieAForm)

#def add_french(request):
 #   return add_team(request ,Ligue1Form)







def edit_english(request ,id):
    return edit_team(request,id ,Premiership ,PremiershipForm)


def edit_spanish(request ,id):
    return edit_team(request,id,Laliga,LaligaForm)

def edit_german(request,id):
    return edit_team(request,id, Bundesliga ,BundesligaForm)

def edit_italian(request,id):
    return edit_team(request,id,ItalianSerieA ,ItalianSerieAForm)

def edit_french(request,id):
    return edit_team(request,id,Ligue1 ,Ligue1Form)

def edit_tuk(request ,id):
    return edit_team(request,id ,Turkey ,TurkeyForm)



def delete_team(request,id):
    Premiership.objects.filter(id=id).delete()
    items =Premiership.objects.all()
    context ={
        'item':items
    }
    return render(request ,'match.html' ,context)    
#class PostUpdateView(UpdateView):

  #  template_name = 'home.html'
  #  form_class = EnglishForm
  #  print('form:' ,form_class)
    #queryset = EnglishLeague.objects.all()
    #print(queryset)
    #success_url='/'
  
    #model = EnglishLeague
    #fields =['team_name' ,'played' ,'win','lost','draw' ,'goalf' ,'goala' ,'point']
    #template_name = 'update.html'


    #def get_object(self):
     #   id = self.kwargs.get('id')
      ## return get_object_or_404(EnglishLeague ,id=id)
      

    #def form_valid(self ,form):
     #   print(form.cleaned_data)
      #  return super().form_valid(form)     


def updateTuk(request, id):
    display =Turkey.objects.get(id =id)
    form =TurkeyForm(request.POST, instance =display)

    print("form:" ,form)
    if request.method == 'POST':
        form =TurkeyForm(request.POST or None, instance =display)
        try:
            if form.is_valid():
                form.save(commit =True)
                messages.success(request ,"successfully updated")
                return redirect('info:matches')
            else:
                print("invalid form ")
        #context = {'form':form}
        except:
            print('not working yet')    

    return render(request ,'matches.html')




def updateData(request, id ,cls,model):
    display = cls.objects.get(id =id)
    form = model(request.POST or None, instance =display)

    print("form:" ,form)
    if request.method == 'POST':
        form = model(request.POST or None, instance =display)
        try:
            if form.is_valid():
                form.save(commit =True)
                messages.success(request ,"successfully updated")
                return redirect('info:matches')
            else:
                print("invalid form ")
        #context = {'form':form}
        except:
            print('not working yet')    

    return render(request ,'matches.html')
  



def edit_team(request ,id,model,cls):
    item = get_object_or_404(model ,id=id)
    if request.method == "POST":
        form =cls(request.POST or None ,instance =item)
        if form.is_valid():
            form.save()
            return redirect('info:matches')  
        else:
            print("invlaid form") 
            print(form)

    else:
        print("form not valid")
        #form =cls(instance =item)  
    return render(request ,'matches.html')  
        

def updateEng(request,id):
    return updateData(request,id,Premiership,PremiershipForm)


#def updateNig(request,id):
 #   return edit_team(request,id,PremierS,PremierSForm)    


def updateGer(request,id):
    return updateData(request,id ,Bundesliga,BundesligaForm)    

def updateSpa(request,id):
    return updateData(request,id ,Laliga,LaligaForm)

def updateIta(request,id):
    return edit_team(request,id ,ItalianSerieA,ItalianSerieAForm)


def updateFre(request,id):
    return edit_team(request,id ,Ligue1,Ligue1Form)  


#def updateTuk(request,id):
    #return edit_team(request,id ,Turkey,TurkeyForm)     


    




def edit(request ,id ,cls):
    display = cls.objects.get(id =id)
    return render(request ,'update.html' ,{'display' :display})



def editPrem(request,id):
    return edit(request,id ,PremierS)

def editEng(request,id):
    return edit(request,id ,Premiership)

def editGer(request,id):
    return edit(request,id ,Bundesliga)


def editSpa(request,id):
    return edit(request,id ,Laliga)

def editIta(request,id):
    return edit(request,id ,ItalianSerieA )


def editFre(request,id):
    return edit(request,id ,Ligue1)  


def editTuk(request,id):
    return edit(request,id ,Turkey)  

#def edit(request ,id):
 #   display = ItalianSerieA.objects.get(id =id)
  #  return render(request ,'update.html' ,{'display' :display})



def insert_view(request):
    form = ItalianLeagueForm()
    if request.method == 'POST':
        form = ItalianSerieAForm(request.POST)
        if form.is_valid():
            form.save()
            print("congratulations!")
            return redirect('/')

    return render(request ,'insert.html' ,{'form': form}) 







#def update_view(request ,id):
    #italy =ItalianLeague.objects.get(id=id)   
    #form = ItalianLeagueForm(request.POST,instance=italy)
 
    #contacts = ContactUs(name=message_name ,phone=message_phone ,email=message_email ,message=message)
    #if form.is_valid():
      #  form.save(commit=True)
     #   print('successful')
    #    return redirect('/')
   # else:
            # Do something in case if form is not valid
     #   raise Http404     
     #   print('form is not valid')  
    #italy = reverse('info:updated', italy.id)      
    #return render(request ,'update.html' ,{'italy' :italy})    




def spainish(request):
    if request.method == 'POST':
        form =SpanishForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request ,"successfully updated")
                return redirect('info:matches')

     
            except:
                messages.error(request ,"not updated")

        else:
            form =SpanishForm()
               
    return render(request ,'top_league.html' ,{'form' :form})


#def updated(request , name):
  #  if request.method =='POST':
      #  eng = EnglishLeague.objects.get(pk =name)
      #  form = EnglishForm(request.POST or None ,instance =eng)

      #  if form.is_valid():
         #   form.save()
     #   return redirect('update.html')   

   # else:
       # eng = EnglishLeague.objects.get(pk = name)     
       # return render(request ,'update.html' ,eng)


def services(request):

    return render(request ,'services.html')

#def registration(request):

 #   return render(request ,'registration.html')

def contact(request):
    if request.method =='POST':
        message_name = request.POST['message-name']
        message_phone = request.POST.get("message-phone" ,False)
        message_email = request.POST['message-email']
        message  = request.POST['message']

        # seend a mail
        send_mail(
            message_name , # email subject
            message ,      # main message
            message_email , # from email 
            [settings.EMAIL_HOST_USER], # recipient, to email
        fail_silently=False)
        
        
        #contacts = ContactUs(name=message_name ,phone=message_phone ,email=message_email ,message=message)
        contacts = ContactUs()
        contacts.name =message_name
        contacts.phone = message_phone
        contacts.email = message_email
        contacts.message = message
        contacts.save()


        return render(request ,'contacts.html',{'message_name' :message_name}) 

    else:
        return render(request ,'contacts.html' ,{})     


def login(request):

    return render(request ,'login.html')       

def logout(request):

    return render(request ,'logout.html')    



# reachgold
def reachgold(request):
    return render(request , 'reachgold.html')



def personal(request):

    return render(request , 'personal.html')
    





