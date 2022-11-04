
from Tools.scripts.var_access_benchmark import A
from django.contrib.auth import authenticate, get_user_model
from django.db.models import Func, F, Value, CharField, Q
from django.http import Http404,HttpResponse
from django.shortcuts import render
from django_filters import filterset
from django_filters.filterset import remote_queryset
from rest_framework.response import Response
# Create your views here.
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import viewsets, status, generics, mixins
from .forms import *
from .pagination import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
import csv
from django.contrib.auth.models import User

# class Instructorlistcreateview(generics.ListCreateAPIView):
#     serializer_class = InstructorSerializer
#     queryset = Instructor.objects.all()
#
#
# class Instructorretrieveupdateview(generics.RetrieveUpdateAPIView):
#     serializer_class = InstructorSerializer
#     queryset = Instructor.objects.all()
#
# class courseretlistcreate(generics.ListCreateAPIView):
#     serializer_class = CourseSerializer
#     queryset = Course.objects.all()

class Modulesserializerlistcreateview(generics.ListCreateAPIView):
    serializer_class = Modulesserializer
    queryset = Modules.objects.all()

class Studjango_filter(generics.ListCreateAPIView):
    queryset = StudentforModule.objects.all()
    serializer_class = StudentforModuleserializers2
    filter_backends = (DjangoFilterBackend,)
    filterset_class=StuformoduleFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]


class Stufilter2(viewsets.ViewSet):
    filter_backends = (DjangoFilterBackend,)
    def list(self,request):
        queryset=StudentforModule.objects.all()
        filter_fields=['name','age']
        search_fields=['=name','age']
        a=StuformoduleFilter(self.request.GET,queryset=queryset)
        serializer=StudentforModuleserializers(a,many=True)
        print(serializer.data)
        return Response(serializer.data)


class StudentforModulelistcreateview(APIView):
    #serializer_class = StudentforModuleserializers
    #queryset = StudentforModule.objects.all()
    pagination_class = CustomPageNumberPagination
    # serializer_class = Modulesserializer
    #queryset = Modules.objects.all()
    authentication_classes = [SessionAuthentication]

    def get(self,request,format=None):

        from datetime import date
        name=request.GET.get('name')
        age=request.GET.get('age')
        search=request.GET.get('search')
        fromid=request.GET.get('fromid')
        toid=request.GET.get('toid')
        namesin=request.GET.get('namesin')
        gt=request.GET.get('gt')
        updateage=request.GET.get('updateage')
        print(name)
        #if (StudentforModule.objects.filter(name=name)).exists() and (StudentforModule.objects.filter(age=age).exists()):
        filters = {}
        if name :
            filters['name'] = name
        if age:
            filters['age']=age
        if search:
            filters['name__contains']=search
        if fromid!=None and toid!=None:
            l=[]
            l.append(fromid)
            l.append(toid)
            filters['created_at_date__range']=l
        if namesin:
            filters['name__in']=list(namesin.split(','))
        if gt:
            filters['created_at_date__gt']=gt

        if updateage:
            student = StudentforModule.objects.filter(**filters).update(age=F('age') + updateage)

        if updateage==None:
            student=StudentforModule.objects.filter(**filters)
        #student = StudentforModule.objects.filter(**filters).values(date=Func(F('created_at'),Value('%d-%m-%Y'),output_field=CharField()))

        #suraj=StudentforModule.objects.filter(name='suraj')
        #print(student,len(student))
        #globaldict=[]

        """
        for i in range(len(student)):
            localdict=dict()
            localdict['id']=student[i].id
            localdict['name']=student[i].name
            localdict['age']=student[i].age
            localdict['grade']=student[i].grade
            sublocaldict=[]
            for j in student[i].modules.all():
                dict1=dict()
                #print("aipoyindi")
                #print("eewwwwwwwwwww",j,j.module_name,j.module_duration,"ggg",j.id)
                obj=Modules.objects.get(id=j.id)
                #print("object is",obj.class_room)
                dict1['id']=obj.id
                dict1['module_name']=obj.module_name
                dict1['module_duration']=obj.module_duration
                dict1['class_room']=obj.class_room
                print(dict1,end="")
                #obj_name=namedtuple("obj name",dict1.keys())(*dict1.values)
                #dict1 = Modules.objects.filter(id=j.id).values
                print(dict1)
                sublocaldict.append(dict1)
            localdict['modules']=sublocaldict
            globaldict.append(localdict)
        print(globaldict)
        """
        if updateage:
            filters['age']=int(age)+int(updateage)
            print("dddduuurr",filters['age'],type(age),type(updateage))
            student = StudentforModule.objects.filter(**filters)
            serializer = StudentforModuleserializers(student, many=True)
            return Response(serializer.data)
        else:
            serializer = StudentforModuleserializers(student, many=True)
            data = serializer.data
            for d in data:
                modules = d['modules']
                m = []
                for id in modules:
                    serializer = Modulesserializer(Modules.objects.get(id=id))
                    m.append(serializer.data)
                d['modules'] = m
            print("ayyo user",request.user)
            return Response(data)

class StudentforModuleretrieveupdateview(generics.RetrieveUpdateAPIView):
    serializer_class = StudentforModuleserializers
    queryset = StudentforModule.objects.all()


# class Courselistview(APIView):
#     serializer_class = CourseSerializer
#     queryset = Course.objects.all()
#     #listing_filter=ProductFilter(request.GET,queryset=queryset)
#     #pagination_class = CustomPageNumberPagination
#
#     # filter_backends = [DjangoFilterBackend]
#     # filterset_class = ProductFilter
#     # pagination_class = CustomPageNumberPagination
#     def get(self,request,Format=None):
#         courses=Course.objects.all()
#         resultset=[]
#         for course in courses:
#             list1=dict()
#             list1['id']=course.id
#             list1['title']=course.title
#             list1['rating']=course.rating
#             name1=course.instructor.name
#             obj=Instructor.objects.get(name=name1)
#             serializer=InstructorSerializer(obj)
#             list1['instructor']=serializer.data
#             resultset.append(list1)
#         print(resultset)
#
#         return Response({'content':resultset})
#
#
#     #filterset_fields =['rating','instructor']
# def contact(request):
#     if request.method == 'POST':
#         form = Contactforms(request.POST)
#         print("komma vijay")
#         if form.is_valid():
#             print("dondi")
#             name=form.cleaned_data['name']
#             email=form.cleaned_data['email']
#             print(name,'ddddd')
#     form=Contactforms()
#     return render(request,'form.html',{'form':form})
#
# def Snippetview(request):
#     if request.method == 'POST':
#         form = Snippetform(request.POST)
#         print("jitendra")
#         if form.is_valid():
#             name=form.cleaned_data['name']
#             email=form.cleaned_data['body']
#             print(name,email,'eeewwww')
#             form.save()
#     form=Snippetform()
#     return render(request,'form.html',{'form':form})

class apiview(APIView):

    def get(self,request,format=None):
        objs=apiviewmodel.objects.all()
        serializers=apiviewmodelserializer(objs,many=True)
        return Response(serializers.data)


    def post(self,request,format=None):
        serializers=apiviewmodelserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)



class apiviewwithkey(APIView):
    def get(self,request,pk,format=None):
        if pk is None:
            objs=apiviewmodel.objects.all()
            serializer=apiviewmodelserializer(objs,many=True)
            return Response(serializer.data)
        else:
            objs=self.get_object(pk)
            serializers=apiviewmodelserializer(objs)
            return Response(serializers.data)

    def get_object(self,pk):
        try:
            return apiviewmodel.objects.get(id=pk)
        except apiviewmodel.DoesNotExist:
            raise Http404

    def put(self,request,pk,format=None):
        objs=self.get_object(pk)
        print("ooo lolliii eeew",request.data)
        serializers=apiviewmodelserializer(objs,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
        objs=self.get_object(pk)
        objs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# def csv_view(request):
#     response=HttpResponse(content_type='text/csv',headers={'Content-Disposition':'attachment;filename="somefilename.csv"'},)
#     writer=csv.writer(response)
#     modules=Modules.objects.all()
#     writer.writerow(['module_name','module_duration','class_room','created_at','updated_at'])
#     for module in modules:
#         writer.writerow([module.module_name,module.module_duration,module.class_room,module.created_at,module.updated_at])
#
#     return response

def csv_view(request):
    response=HttpResponse(content_type='text/csv',headers={'Content-Disposition':'attachment;filename="somefilename.csv"'},)
    writer=csv.writer(response)
    modules=StudentforModule.objects.all()
    writer.writerow(['name','age','grade','modules','created_at','updated_at'])
    for Sfmodule in modules:
        list1=Sfmodule.modules.all()
        print("durrrrr",list1,type(list1))
        list2=[]
        for obj in list1:
            serializer=Modulesserializer(Modules.objects.get(id=obj.id))
            list2.append(serializer.data)
        writer.writerow([Sfmodule.name,Sfmodule.age,Sfmodule.grade,list2,Sfmodule.created_at,Sfmodule.updated_at])

    return response

class Authclassview(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = Auth_class_serializer
    queryset=Authmodel.objects.all()

class auth_user_testing(mixins.UpdateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    serializer_class = Auth_class_serializer
    queryset = Authmodel.objects.all()

class usertoken(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def post(self,request):
        refresh = RefreshToken.for_user(request.user)
        print(request.user)
        return Response({'refresh': str(refresh),'access': str(refresh.access_token)})

#####
class custom_auth(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return Response({'detail':'You have already authenticated'},status=400)
        data=request.data
        username=data.get('username')
        password=data.get('password')
        #user=authenticate(username=username,password=password)
        qs=User.objects.filter(
            Q(username__iexact=username)
        ).distinct()
        if qs.count()==1:
            user_obj=qs.first()
            if user_obj.check_password(password):
                refresh = RefreshToken.for_user(request.user)
                print(request.user)
                return Response({'refresh': str(refresh), 'access': str(refresh.access_token),'user':username,'password':password})

        return Response({"detail":"Invalid credentials"},status=401)


# class City_view(APIView):
#     serializers=City_Serializer
#     queryset=City.objects.all()
#
#     def get(self,request):
#         print("eeww")
#         cities=City.objects.all().select_related('province')
#         cnt=0
#         for city in cities:
#             print(city.name,city.province.name)
#             cnt+=1
#         return Response({"count":cnt})

class City_view(generics.ListCreateAPIView):
    serializer_class = City_Serializer
    queryset=City.objects.all()

class Books_view(APIView):
    serializers=Books_Serializer
    queryset=Books_model.objects.all()

    def get(self,request):
        print("eeww")
        books=Books_model.objects.all().prefetch_related('storeset')
        cnt=0
        list1=dict()
        for book in books:
            print(book.name,book.storeset.all())
            store=[]
            for bookstore in book.storeset.all():
                serializer=Store_Serializer(bookstore)
                store.append(serializer.data)
            list1[''+str(book.name)]=store

            cnt+=1
        return Response({"count":cnt,'content':list1})
class test_book_view(generics.ListCreateAPIView):
    serializer_class = Books_Serializer
    queryset = Books_model.objects.all()

class Outerjoin(APIView):
    serializers=Books_model
    queryset=Books_model.objects.all()

    def get(self,request,format=None):
        books=Books_model.objects.all()
        resultset=dict()
        count=0
        for book in books:
            count+=1
            if book.storeset.all() is None:
                print(book.name,None)
                resultset[''+book.name]=None
            else:
                l=[]
                for bookstore in book.storeset.all():
                    serializer=Store_Serializer(bookstore)
                    l.append(serializer.data)
                resultset[''+str(book.name)]=l
        print(resultset)
        return Response({'count':count,'data':resultset})


class Studentviewset(viewsets.ViewSet):
    def list(self,request):
        queryset=employee.objects.all()
        serializer=employee_serializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            queryset=employee.objects.get(id=id)
            serializer=employee_serializer(queryset)
            return Response(serializer.data)

    def update(self,request,pk):
        id=pk
        queryset = employee.objects.get(pk=id)
        serializer = employee_serializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        id=pk
        queryset=employee.objects.get(pk=id)
        queryset.delete()
        return Response({'msg':'deleted'})
    def create(self,request):
        serializer=employee_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data created'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class courseviewset(viewsets.ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
# class Instructorviewset(viewsets.ModelViewSet):
#     queryset = Instructor.objects.all()
#     serializer_class = InstructorSerializer
#
# ### here hyperlinked model serializer is used
# class course_detail_view(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class Instructor_detail_view(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Instructor.objects.all()
#     serializer_class = InstructorSerializer

class user_detail_view(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = User_serializer


class ArticleView(APIView):
    queryset = Article.objects.all()
    serializer_class = article_serializer


class publications_view(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = Publication_serializer

    def get(self,request,Format=None):
        publications=Publication.objects.all()
        list1=[]
        for publication in publications:
            l=dict()
            l['id']=publication.id
            l['publisher_name']=publication.title
            articles=publication.Article_set.all()

            list2=[]
            for article in articles:
                l1 = dict()
                l1['headline']=article.headline
                l1['article']=article.article
                list2.append(l1)
            l['articles']=list2
            list1.append(l)
        return Response({'content':list1})

class Women_views(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = Women_serializer


class Student_view(generics.ListCreateAPIView):
    queryset=StudentforModule.objects.all()
    serializer_class = StudentforModuleserializers2


class Language_view(generics.ListCreateAPIView):
    queryset=Languages.objects.all()
    serializer_class = Languages_serializer


class Sports_view(generics.ListCreateAPIView):
    queryset = Sports.objects.all()
    serializer_class = Sports_serializer


class percentmodulecomplete_view(generics.ListCreateAPIView):
    queryset = Percent_Module_Complete.objects.all()
    serializer_class = percent_modulecomplete_serializer

class Studentwithsportsandlanguages_view(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class =Student_serializer


class Courseforstudent_view(generics.ListCreateAPIView):
    queryset=CourseforStudent.objects.all()
    serializer_class =courseforStudent_serializer


class Enrollement_view(generics.ListCreateAPIView):
    queryset=Enrollement.objects.all()
    serializer_class = Enrollement_serializer


class Enrollement_view_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollement.objects.all()
    serializer_class = Enrollement_serializer



