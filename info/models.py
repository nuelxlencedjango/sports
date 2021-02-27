from django.db import models
from phone_field import PhoneField
import datetime
#from django.utils.timezone.now
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField()
    date_posted =models.DateTimeField(default=timezone.now)
    dated = datetime.datetime.now()
    author  = models.ForeignKey(User ,on_delete=models.CASCADE)
    img = models.ImageField(default='manprof.png' , upload_to='images')
    
    # without s
    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title   #, 'by', self.author

    #post detail
    def get_absolute_url(self):
        return reverse('post-detail' ,kwargs={'pk' :self.pk})   



class Position(models.Model):
    title =models.CharField(max_length =20)

    def __str__(self):

        return self.title

    class Meta:
        verbose_name_plural = "Playing Position"    



class PlayersRegistration(models.Model):
    first_name =models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    position =models.ForeignKey(Position ,on_delete =models.CASCADE ,default=False)  
    email = models.EmailField(unique =True ,blank=False)
    image = models.ImageField(blank=False,upload_to='images')

    def __str__(self):
        return self.last_name




class News(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField()
    date_posted = models.DateTimeField(auto_now_add = False ,auto_now =False) 
    img = models.ImageField(default='manprof.png' , upload_to='images')
    
   # def get_absolute_url(self):
    #    return "news_detail/id".format(id=self.id)
    class Meta:
        verbose_name_plural = "News"

    def __str__(self):

        return self.title


class Training(models.Model):
    #title = models.CharField(max_length=100)
    #content =models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True) 
    img = models.ImageField(default='manprof.png' , upload_to='images')
    

    class Meta:
        verbose_name_plural = "Training"

   # def __str__(self):

    #    return self.date_posted

class Coach(models.Model):
    name = models.CharField(default = 'coach' ,max_length=50)
    position =models.CharField(max_length = 50)
    about = models.TextField(max_length=100)
    img = models.ImageField(default='manprof.png' , upload_to='images')
    

    class Meta:
        verbose_name_plural = "Our Coaches"
    def __str__(self):

        return self.name 



class Competition(models.Model):

    class Meta:
        verbose_name_plural = "Competition"
    name = models.CharField(max_length=100) 
    def __str__(self):
        return self.name
  
class ImportantMatches(models.Model):
    home_team =  models.CharField(max_length=100) 
    away_team =  models.CharField(max_length=100)
    matchday = models.DateTimeField(default=timezone.now)
    competition_name = models.ForeignKey(Competition ,on_delete =models.CASCADE ,default=False)                
   
    def __str__(self):
        return self.competition_name.name

    class Meta:
        verbose_name_plural = "Important Matches"
      
 

class ContactUs(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField(unique = False) 
    phone = models.CharField(max_length=20) 
    message = models.TextField(max_length=100)


    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.name
 


# european leagues

#class Point(models.Model):
 #   gained_point = models.CharField(max_length=1 ,unique=False)  

    
  #  def __str__(self):
   #     return self.gained_point  

class League(models.Model):
    league_name = models.CharField(max_length=50, unique = False) 

    def __str__(self):
        return self.league_name 

class WorldLeague(models.Model): 
    league = models.ForeignKey(League,default=1,verbose_name="League", on_delete =models.SET_DEFAULT) 
    #league = models.ForeignKey(League,default=1,verbose_name="League" on_delete =models.CASCADE)                                        
    played =models.IntegerField() 
    win = models.IntegerField() 
    draw = models.IntegerField()
    lost = models.IntegerField() 
    goalf = models.IntegerField() 
    goala = models.IntegerField() 
    point = models.IntegerField(default=0)

    class Meta:
        abstract =True

    def __str__(self):
        return self.league.league_name           

       

class EnglishClubs(models.Model):
    team = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return self.team

    class Meta:
        verbose_name_plural = "EnglishClubs"    


class Premiership(WorldLeague):
    team_name = models.ForeignKey(EnglishClubs, models.CASCADE,default=None)  
    
    def __str__(self):
        return self.team_name.team

    class Meta:
        verbose_name_plural = "Premiership"      



class SpanishClubs(models.Model):
    team = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return self.team

    class Meta:
        verbose_name_plural = "SpanishClubs" 



class Laliga(WorldLeague):
    team_name = models.ForeignKey(SpanishClubs, models.CASCADE,default=None)  
    
    def __str__(self):
        return self.team_name.team

    class Meta:
        verbose_name_plural = "Laliga"        


class GermanClubs(models.Model):
    team = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return self.team

    class Meta:
        verbose_name_plural = "GermanClubs"  



class Bundesliga(WorldLeague):
    team_name = models.ForeignKey(GermanClubs, models.CASCADE,default=None)  
    
    def __str__(self):
        return self.team_name.team

    class Meta:
        verbose_name_plural = "Bundesliga"        


class ItalianClubs(models.Model):
    team = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return self.team
 
    class Meta:
        verbose_name_plural = "ItalianClubs"     



class ItalianSerieA(WorldLeague):
    team_name = models.ForeignKey(ItalianClubs, models.CASCADE,default=None)  
    
    def __str__(self):
        return self.team_name.team

    class Meta:
        verbose_name_plural = "ItalianSerieA"                              


class FrenchClubs(models.Model):
    team = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return self.team

    class Meta:
        verbose_name_plural = "FrenchClubs"  



class Ligue1(WorldLeague):
    team_name = models.ForeignKey(FrenchClubs, models.CASCADE,default=None)  
    
    def __str__(self):
        return self.team_name.team

    class Meta:
        verbose_name_plural = "Ligue1"        

        



#league = models.ForeignKey(League,default=1,verbose_name="League" on_delete =models.CASCADE) 
  
         

#myList.sort(reverse=True);       






#class Bundesliga(WorldLeague):
    #team =  models.ForeignKey(EnglishClubs ,on_delete =models.CASCADE ,default=1)  
  
    #team_name=models.ForeignKey(GermanClubs ,on_delete =models.CASCADE ,default=False)                           

    #class Meta:
     #   verbose_name_plural ="Bundesliga"

   # def __str__(self):
    #    return self.team_name    





      


#class Ligue1(WorldLeague):
    #team_name =  models.ForeignKey(FrenchClubs ,on_delete =models.CASCADE ,default=False)                           
  
   # class Meta:
      #  verbose_name_plural ="Ligue1"

  

       #db_table ="SerieA"

    #def __str__(self):
    #    return self.team_name  
  


#class Premiership(models.Model):
  
 #   team = models.CharField(max_length=50,unique=True) 
  #  class Meta:
   #     verbose_name_plural = "Premiership Teams"
     
    #class Meta:
     #   order_with_respect_to = 'id'

    #def __str__(self):
     #   return self.team

        
 


#DATABASE QUEERYSET 
 # from django.db import models
 #from django.contrib.auth.models import User
 # User.objects.all() -to fetch all data 
 # User.objects.first() -first value
 # User.objects.filter(id=id or username="nuel")
 # User.objects.filter(id=id or username="nuel").first () first value from the row
 #User.id ,User.pk
 # use = User.objects.get(id=id) - get the id of the product
 #use.save()

    