
from django.urls import path
from .views import *
from .import views 




app_name ="info"

urlpatterns = [
  
    path('' ,PostListView.as_view() ,name='home'),

    path('<int:pk>/' , PostDetailView.as_view() ,name="detail"),
    path('news_detail/<int:pk>/' ,NewsDetailView.as_view() ,name="news_detail"),

     path('' ,NewsListView.as_view() ,name='home'),
  

    path('' ,TrainListView.as_view() ,name='home'),
   
    #path('post/new/' , PostCreateView.as_view() ,name="create"),

    #path('post/<int:pk>/delete/' , PostDeleteView.as_view() ,name="delete"),
    path('user/<str:username>' , UserPostListView.as_view() ,name="posts"),


#edit
 path('editEng/<int:id>/',views.editEng ,name='editEng'),
 path('editGer/<int:id>/',views.editGer ,name='editGer'),
 path('editSpa/<int:id>/',views.editSpa ,name='editSpa'),
 path('editIta/<int:id>/',views.editIta ,name='editIta'),
 path('editFre/<int:id>/',views.editFre ,name='editFre'),


#update
 #path('updateNig/<int:id>/',views.updateNig ,name='updateNig'),
 path('updateEng/<int:id>/',views.updateEng ,name='updateEng'),
 path('updateGer/<int:id>/',views.updateGer ,name='updateGer'),
 path('updateSpa/<int:id>/',views.updateSpa ,name='updateSpa'),
 path('updateIta/<int:id>/',views.updateIta ,name='updateIta'),
 path('updateFre/<int:id>/',views.updateFre ,name='updateFre'),


    path('matches/' , MatchView.as_view() ,name="matches"),
    path('edit/<int:id>/',views.edit ,name='edit'),

    path('updated/<int:id>/',views.updateData ,name='updated'),

   # path('english/',views.insert_english ,name='english'),
    #path('italy/' , views.insert_italy ,name="italy"),
    #path('germany/',views.insert_germany ,name='germany'),
    #path('france/' ,views.insert_france ,name="france"),
    #path('spain/',  views.insert_spain ,name='spain'),


   path('delete_item/',  views.delete_team ,name='delete_item'),


   # path('add_english/',views.add_english ,name='add_english'),
    #path('add_italy/' , views.add_italian ,name="add_italy"),
    #path('add_germany/',views.add_german ,name='add_germany'),
    #path('add_france/' ,views.add_french ,name="add_france"),
    #path('add_spain/',  views.add_spanish ,name='add_spain'),

    
    path('edit_english/<int:id>/',views.edit_english ,name='edit_english'),
    path('edit_italy/<int:id>/' , views.edit_italian,name="edit_italy"),
    path('edit_germany/<int:id>/',views.edit_german ,name='edit_germany'),
    path('edit_france/<int:id>/' ,views.edit_french ,name="edit_france"),
    path('edit_spain/<int:id>/',  views.edit_spanish ,name='edit_spain'),

  path('add_team/',  views.add_team ,name='add_team'),

   path('players_info/' , PlayersView.as_view() ,name="players_info"),


    path('search/', views.search , name='search'),
    path('about/',views.about ,name='about'),
    path('training/',TrainListView.as_view() ,name='training'),
    path('registration/',views.registration ,name='registration'),
    path('contact/',views.contact ,name='contact'),
    path('mission/',views.mission ,name='mission'),
 
    path('services/',views.services ,name='services'),
  



    
]

