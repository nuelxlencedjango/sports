from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class PlayersForms(forms.ModelForm):
    
    class Meta:

        model =  PlayersRegistration
        fields = '__all__' 
        #fields = ['firstname','lastname' ,'email' ,'phone_number' ,'address' ,'position' ,'img']  
        labels ={
            'first_name' :'First Name',
             'last_name' :'Last Name',
            'address' : 'Address',
            'position': 'Playing Position',
            'email' :'Email',
            'phone' :'Phone Number',
            'image' :'Upload Your Photo',
            #'img': 'your pic'       
        }
        #selecting an item from drop down
    def __init__(self ,*args ,**kwargs):

        super(PlayersForms ,self).__init__(*args ,**kwargs)
        self.fields['position'].empty_label ='select'
           #self.fields['2nd phone number'].required =False




class PremiershipForm(forms.ModelForm):

    class Meta:
       model =Premiership
       fields = ['team_name' ,'played' ,'win' ,'draw' ,'lost','goalf' ,'goala' ,'point']



class BundesligaForm(forms.ModelForm):
       model = Bundesliga
       fields = ['team_name' ,'played' ,'win' ,'draw' ,'lost','goalf' ,'goala' ,'point']
 
class LaligaForm(forms.ModelForm):
    class Meta:
        model = Laliga
        fields = ['team_name' ,'played' ,'win' ,'draw' ,'lost','goalf' ,'goala' ,'point']


class ItalianSerieAForm(forms.ModelForm):
    class Meta:
        model = ItalianSerieA
        fields = ['team_name' ,'played' ,'win' ,'draw' ,'lost','goalf' ,'goala']
                    

class Ligue1Form(forms.ModelForm):
    class Meta:
        model = Ligue1
        fields = ['team_name' ,'played' ,'win' ,'draw' ,'lost','goalf' ,'goala' ]
                          
#class PlayersRegForm(forms.ModelForm):
  #  """Form for the image model"""
    #class Meta:
      #  model = PlayersReg
        #fields = ('first_name','last_name' ,'email' ,'phone' ,'address' ,'position' ,'image')  
       
#class PlayerRegisterForm(forms.Form):
    #firstname = forms.CharField(max_length = 200) 
    #lastname = forms.CharField(max_length = 200) 
    #phone_number = forms.IntegerField( help_text = "Enter 6 digit roll number"
     #                )
    #email = forms.EmailField()
    #password1 = forms.CharField(widget = forms.PasswordInput()) 
    #password2 =forms.CharField()
    
