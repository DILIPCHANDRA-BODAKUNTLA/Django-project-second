from django.db import models
from django.utils.timezone import now
from django.conf import settings
from django.urls import reverse
# Create your models here.
# class Instructor(models.Model):
#     name=models.CharField(max_length=40,null=True,blank=True)
#     email=models.EmailField(null=True,blank=True)
#     #instructor_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='a', null=True, blank=True)
#     def __str__(self):
#         return self.email
#     # @property
#     # def courses(self):
#     #     return self.course_set.all()
#
# class Course(models.Model):
#     title = models.CharField(max_length=30,null=True,blank=True)
#     rating=models.IntegerField()
#     instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE,null=True,blank=True,related_name='courseset')
#
#     class Meta:
#         unique_together=('title','instructor')


class Publication(models.Model):
    title = models.CharField(max_length=30,null=True,blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100,null=True,blank=True)
    article=models.IntegerField()
    publications = models.ManyToManyField(Publication,null=True,blank=True,related_name='Article_set')

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline
class snippet(models.Model):
    name=models.CharField(max_length=100)
    body=models.TextField()
    def __str__(self):
        return self.name



class apiviewmodel(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    password=models.CharField(max_length=30,null=True,blank=True)


class DatetoChar(models.Func):
    arity=2
    function = 'to_char'
    output_field =models.CharField()

class Authmodel(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    study=models.CharField(max_length=30)

class Province(models.Model):
    name=models.CharField(max_length=30)

class City(models.Model):
    name=models.CharField(max_length=30)
    commissioner=models.CharField(max_length=30)
    province=models.ForeignKey(Province,blank=True,null=True,related_name='city_set',on_delete=models.CASCADE)

class Books_model(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()

class Store_model(models.Model):
    name=models.CharField(max_length=30)
    books=models.ManyToManyField(Books_model,blank=True,null=True,related_name='storeset')


class employee(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()

    def get_absolute_url(self):
        return reverse("apiviewwithkey",kwargs={"id":self.id})


class Men(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()

class Women(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    relation=models.OneToOneField(Men,related_name='Women_set',on_delete=models.CASCADE)


#///////////////////////////////@@@@@@@@@@@@@@@@@
class Sports(models.Model):
    sport_name=models.CharField(max_length=40)
    #sport_coach=models.CharField(max_length=40)

    def __str__(self):
        return self.sport_name



class Percent_Module_Complete(models.Model):
    percent_complete=models.IntegerField()

    def __str__(self):
       return str('modulecompletedupto'+str(self.percent_complete)+'percent')

class Modules(models.Model):
    from datetime import datetime
    module_name=models.CharField(max_length=100)
    module_duration=models.IntegerField()
    class_room=models.IntegerField()
    created_at=models.DateTimeField(null=True,blank=True,editable=True)
    updated_at=models.DateTimeField(null=True,blank=True,editable=True,default=datetime.now())
    percentage_completion=models.OneToOneField(Percent_Module_Complete,null=True,blank=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name

    @property
    def modules(self):
        return self.Modules_set.all()



class Languages(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name


class StudentforModule(models.Model):
    from datetime import datetime
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    grade=models.IntegerField()
    modules=models.ManyToManyField(Modules,related_name='studentwithmodule')
    created_at=models.DateTimeField(null=True,blank=True,editable=True)
    updated_at=models.DateTimeField(null=True,blank=True,editable=True,default=datetime.now())
    sports_registered = models.ManyToManyField(Sports,null=True,blank=True,related_name='Studentformodule_set')
    marks=models.IntegerField(null=True,blank=True)
    languages_spoken=models.ManyToManyField(Languages,null=True,blank=True)
    #created_at_date=models.DateField(null=True,blank=True,editable=True)


    def __str__(self):
        return self.name


#///////########another student model


class Student(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.CharField(max_length=30)
    languages_spoken=models.ManyToManyField(Languages,null=True,blank=True,related_name='Studentsetfor_languages')
    sports=models.ManyToManyField(Sports,null=True,blank=True,related_name='Studentsetfor_sports')

    def __str__(self):
        return self.name

class CourseforStudent(models.Model):
    name=models.CharField(max_length=30)
    students=models.ManyToManyField(Student,null=True,blank=True,through='Enrollement',related_name='CourseforStudent_set')

    def __str__(self):
        return self.name


class Enrollement(models.Model):
    course=models.ForeignKey(CourseforStudent,on_delete=models.CASCADE,null=True,blank=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateField()
    completion=models.IntegerField()

    class Meta:
        unique_together=[['course','student']]




# a=a[1].update(headline='politics in telengana',article=5)
# a=Article.objects.filter(headline='politics').update(headline='politics in telengana',article=5)
# updated = Article.objects.update_or_create(headline='cinema news', article=4,defaults={'headline':'cinema-news in telangana','article':40})
#
# updated = Article.objects.update_or_create(headline='sports', defaults={'headline':'sports in telangana','article':100})
