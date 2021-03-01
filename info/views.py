

from django.shortcuts import render ,redirect ,get_object_or_404
from django.views.generic.base import TemplateView

from django.views.generic import (
    ListView ,DetailView, CreateView, UpdateView ,DeleteView
)
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from .models import *
from .forms import * 
from django.http import Http404

from django.contrib import messages
from django.db.models import Q 

# email setting
from django.core.mail import send_mail
from django.conf import settings




class NewsListView(ListView):
 
    template_name = ".html"  # template name/path
    context_object_name ="post" # context properties
    ordering =['-date_posted']   # arraned according date posted
    paginate_by =5



class TrainListView(ListView):
    model = Training # model name
    template_name = 'training.html'  # template name/path
    context_object_name ='training' # context properties
    ordering =['-date_posted']   # arrange according date posted

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
        return context




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

 


def updateGer(request,id):
    return updateData(request,id ,Bundesliga,BundesligaForm)    

def updateSpa(request,id):
    return updateData(request,id ,Laliga,LaligaForm)

def updateIta(request,id):
    return edit_team(request,id ,ItalianSerieA,ItalianSerieAForm)


def updateFre(request,id):
    return edit_team(request,id ,Ligue1,Ligue1Form)  


    




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



def insert_view(request):
    form = ItalianLeagueForm()
    if request.method == 'POST':
        form = ItalianSerieAForm(request.POST)
        if form.is_valid():
            form.save()
            print("congratulations!")
            return redirect('/')

    return render(request ,'insert.html' ,{'form': form}) 









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




def services(request):
    return render(request ,'services.html')


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
    



def about(request):

    return render(request ,'about.html')


def mission(request):
    return render(request ,'mission.html')

def training(request):

    return render(request ,'training.html')



