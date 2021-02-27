from django.contrib import admin


from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content','date_posted','author']

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','content' ,'date_posted']

class TrainAdmin(admin.ModelAdmin):
    list_display = ['img' ,'date_posted']

class CoachAdmin(admin.ModelAdmin):
    list_display = ['name','position' ,'about']

class ImportantMatchesAdmin(admin.ModelAdmin):
    list_display = ['home_team','away_team','matchday']

class RegisterAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','address', 'phone_number' ,'email' ,'position' ,'img' ,'image']


class PlayersRegAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','address', 'phone' ,'email' ,'position' ,'image']


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','phone' ,'email', 'message']


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['id','name' ]

class PositionAdmin(admin.ModelAdmin):
    list_display = ['id','title' ]


class PremiershipClubsAdmin(admin.ModelAdmin):
    list_display = ['id','team'] 
class PremiershipAdmin(admin.ModelAdmin):
    list_display = ['team_name','played','win','draw','lost','goalf','goala','point' ]      
         

class SpanishClubsAdmin(admin.ModelAdmin):
    list_display = ['id','team'] 
class LaligaAdmin(admin.ModelAdmin):
    list_display = ['team_name','played','win','draw','lost','goalf','goala','point' ]      
          

class GermanClubsAdmin(admin.ModelAdmin):
    list_display = ['id','team'] 
class BundesligaAdmin(admin.ModelAdmin):
    list_display = ['team_name','played','win','draw','lost','goalf','goala','point' ]      
          

class ItalianClubsAdmin(admin.ModelAdmin):
    list_display = ['id','team'] 
class ItalianSerieAAdmin(admin.ModelAdmin):
    list_display = ['team_name','played','win','draw','lost','goalf','goala' ]      
          

class FrenchClubsAdmin(admin.ModelAdmin):
    list_display = ['id','team']
class Ligue1Admin(admin.ModelAdmin):
    list_display = ['team_name','played','win','draw','lost','goalf','goala' ]      
                              
   



class LeagueAdmin(admin.ModelAdmin):
    list_display = ['id','league_name' ] 

 #fields =['id','team_name' ,'played']
    #list_filter =['total_point' ,'goalf']
    # search_fields =['price' ,'product_name']

admin.site.register(Training ,TrainAdmin)
admin.site.register(Post ,PostAdmin)
admin.site.register(News ,NewsAdmin)

admin.site.register(Position ,PositionAdmin)
admin.site.register(Coach ,CoachAdmin)
admin.site.register(ImportantMatches , ImportantMatchesAdmin)

admin.site.register(ContactUs , ContactUsAdmin)

admin.site.register(Competition , CompetitionAdmin)

admin.site.register(PlayersRegistration , PlayersRegAdmin)


admin.site.register(League ,LeagueAdmin)



admin.site.register(EnglishClubs,PremiershipClubsAdmin)
admin.site.register(Premiership ,PremiershipAdmin)


admin.site.register(SpanishClubs,SpanishClubsAdmin)
admin.site.register(Laliga ,LaligaAdmin)


admin.site.register(GermanClubs,GermanClubsAdmin)
admin.site.register(Bundesliga,BundesligaAdmin)


admin.site.register(ItalianClubs,ItalianClubsAdmin)
admin.site.register(ItalianSerieA,ItalianSerieAAdmin)

admin.site.register(FrenchClubs,FrenchClubsAdmin)
admin.site.register(Ligue1,Ligue1Admin)
# Register your models here.