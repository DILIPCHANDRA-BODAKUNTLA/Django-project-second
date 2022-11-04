from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter()
router.register(r'authusertesting',auth_user_testing,basename='nothing')
urlpatterns = [
 # path('instructors',Instructorlistcreateview.as_view()),
 # path('instructorsupdate/<int:pk>',Instructorretrieveupdateview.as_view()),
 #path('Stumodule', StudentforModulelistcreateview),
#path('module', Modulesserializerlistcreateview.as_view()),
 #path('Stumodule',StudentforModulelistcreateview.as_view()),
 #path('Stumoduleupdate/<int:pk>', StudentforModuleretrieveupdateview.as_view()),
 # path('cour',Courselistview.as_view()),
 # path('forms',contact),
 #path('Stumodule',StudentforModulelistcreateview.as_view()),

 path('apiview', apiview.as_view(),name='apiview'),
 path('apivi/<int:pk>',apiviewwithkey.as_view(),name='apiviewwithkey'),
 path('csv_view',csv_view),
 #path('Stufilter',Studjango_filter.as_view()),
 #path('stufilter2',Stufilter2.as_view({'get':'list'})),
 path('Authclass',Authclassview.as_view()),
 path('usertoken',usertoken.as_view()),
 path('custom_auth',custom_auth.as_view()),
 path('city_view',City_view.as_view()),
 path('book_view', Books_view.as_view()),
path('testing_book_view', test_book_view.as_view()),
 path('Outerjoin_view', Outerjoin.as_view()),
# path('Studentviewset', Studentviewset.as_view({'get':('list' or 'retrieve')})),
 # path('cour/<int:pk>',course_detail_view.as_view(),name='course-detail'),
 # path('Instructors/<int:pk>', Instructor_detail_view.as_view(), name='instructor-detail'),
 path('User_view', user_detail_view.as_view(), name='user-detail'),
 path('authuser_testing_ulr',include(router.urls)),
 path('articleview', ArticleView.as_view()),
 path('publicationview', publications_view.as_view()),
 path('Women_view', Women_views.as_view()),
 #path('Student_view', Student_view.as_view()),
 path('modulecompletionmodel',percentmodulecomplete_view.as_view()),
 path('sports_view',Sports_view.as_view()),
 path('Languages_view', Language_view.as_view()),
 path('Enrollmentview',Enrollement_view.as_view()),
 path('Enrollmentview_update/<int:pk>', Enrollement_view_update.as_view()),
 path('Student_view', Studentwithsportsandlanguages_view.as_view()),
 path('Courses_view', Courseforstudent_view.as_view()),
 #path('modelforms',Snippetview),
]
