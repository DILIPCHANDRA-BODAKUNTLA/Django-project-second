from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

# class CourseSerializer(serializers.HyperlinkedModelSerializer):
#     #a=InstructorSerializer()
#     #id=serializers.IntegerField(required=False)
#     class Meta:
#         model = Course
#         fields = ['url','id','title','rating']
#
# class InstructorSerializer(serializers.HyperlinkedModelSerializer):
#     courseset = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name = 'course-detail')
#     #uri = serializers.SerializerMethodField(read_only=True)
#     #courseset_id=serializers.PrimaryKeyRelatedField(source='courseset',read_only=True)
#     #course_title=serializers.HyperlinkedRelatedField(source='Course__title',lookup_field='title',view_name='courselist:detail',read_only=True)
#     class Meta:
#         model = Instructor
#         fields=['id','url','name','email','courseset']
#
#     def create(self,validated_data):
#         courses=validated_data.pop('courses')
#         Instructor1 = Instructor.objects.create(**validated_data)
#         for choice in courses:
#             Course.objects.create(instructor=Instructor1,**choice)
#         return Instructor1
#
#     def update(self,instance,validated_data):
#         print(validated_data)
#         #courses=validated_data.pop('courses')
#         courses = validated_data['courses']
#         print(type(courses),courses)
#         print(validated_data)
#         #instance.name = validated_data.get("name",instance.name)
#         print("ooooooooooooooooo")
#         print(instance.courses)
#         instance.save()
#         keep_choices =[]
#         print("eeeew",type(instance.courses),instance.courses)
#         Instructor1 = Instructor.objects.create(**validated_data)
#         #existing_ids=[c.id for c in instance.courses]
#         #print(existing_ids)
#         for choice in courses:
#             if "id" in choice.keys() and Course.objects.filter(id=choice["id"]).exists():
#                     c=Course.objects.get(id=choice["id"])
#                     c.title=choice.get('title',c.title)
#                     c.save()
#                     keep_choices.append(c.id)
#                 # else:
#                 #     continue
#             else:
#                 c=Course.objects.create(instructor=Instructor1,**choice)
#                 c.save()
#                 keep_choices.append(c.id)
#
#         for choice in instance.courses:
#             if choice.id not in keep_choices:
#                 choice.delete()
#
#         return instance
#
#

class Modulesserializer(serializers.ModelSerializer):
    #studentwithmodule=StudentforModuleserializers(many=True)
    class Meta:
        model=Modules
        fields="__all__"

class StudentforModuleserializers2(serializers.ModelSerializer):
    modules=Modulesserializer(many=True)
    class Meta:
        model=StudentforModule
        fields = ['name', 'age', 'grade','modules']

class StudentforModuleserializers(serializers.ModelSerializer):
    modules=Modulesserializer(many=True)
    class Meta:
        model=StudentforModule
        fields=['modules','name','age','grade']
        #fields="__all__"

    def create(self, validated_data):
        modules = validated_data['modules']
        #modules=validated_data.pop('modules')
        print(modules)
        print(validated_data)
        Stumod=StudentforModule.objects.create(**validated_data)
        print(Stumod)
        Stumod.save()
        for i in modules:
            x=Modules.objects.get(module_name=i["module_name"])
            Stumod.modules.add(x)

        return Stumod

    def update(self,instance,validated_data):
        if StudentforModule.objects.filter(name=validated_data['name']).exists():
            modules = validated_data['modules']
            queryset1 = StudentforModule.objects.get(name=validated_data['name'])
            queryset1.age=validated_data['age']
            queryset1.grade=validated_data['grade']
            queryset1.save()
            print(queryset1.name, queryset1.age, queryset1.grade)
            # print(a.modules)
            l1 = []
            for module in modules:
                if "id" in module.keys():
                    if Modules.objects.filter(id=module["id"]).exists():
                        c = Modules.objects.get(id=module["id"])
                        c.module_name = module.get('module_name', c.module_name)
                        c.module_duration = module.get('module_duration', c.module_duration)
                        c.class_room = module.get('class_room', c.class_room)
                        #c.save()
                        l1.append(c.id)
                    else:
                        pass

                else:
                    b = Modules.objects.create(**module)
                    queryset1.modules.add(b)
                    #queryset1.save()
                    l1.append(b.id)



            return queryset1

        else:
            modules=validated_data['modules']
            #modules = validated_data.pop('modules')
            a=StudentforModule.objects.create(**validated_data)
            a.save()
            l=[]
            #idsininstance=[i["id"] for i in modules]
            for j in modules:
                if "id" in j.keys():
                    if Modules.objects.filter(id=j["id"]).exists():
                        c=Modules.objects.get(id=j["id"])
                        c.module_name=j.get('module_name',c.module_name)
                        c.module_duration=j.get('module_duration',c.module_duration)
                        c.class_room=j.get('class_room',c.class_room)
                        c.save()
                        l.append(c.id)
                    else:
                        pass

                else:
                    b=Modules.objects.create(**j)
                    a.modules.add(b)
                    a.save()
                    l.append(b.id)


            return a

class apiviewmodelserializer(serializers.ModelSerializer):
    class Meta:
        model=apiviewmodel
        fields="__all__"


class Auth_class_serializer(serializers.ModelSerializer):
    class Meta:
        model=Authmodel
        fields="__all__"
        #read_only_fields=['user']

class Province_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Province
        fields="__all__"

class City_Serializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields="__all__"

class Books_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Books_model
        fields="__all__"

class Store_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Store_model
        fields=['id',"name"]

class employee_serializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields="__all__"

class User_serializer(serializers.ModelSerializer):
    #password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['username','email','password']


class Publication_serializer(serializers.ModelSerializer):
    class Meta:
        model=Publication
        fields="__all__"


class article_serializer(serializers.ModelSerializer):
    publications=Publication_serializer(many=True)
    class Meta:
        model=Article
        fields=['id','headline','article','publications']


class Men_serializer(serializers.ModelSerializer):
    class Meta:
        model=Men
        fields='__all__'


class Women_serializer(serializers.ModelSerializer):
    relation = Men_serializer()
    class Meta:
        model=Women
        fields=['id','name','age','relation']


class Sports_serializer(serializers.ModelSerializer):
    class Meta:
        model = Sports
        fields=['sport_name']


class Languages_serializer(serializers.ModelSerializer):
    class Meta:
        model=Languages
        fields=['name']


class percent_modulecomplete_serializer(serializers.ModelSerializer):
    class Meta:
        model=Percent_Module_Complete
        fields='__all__'


class Student_serializer(serializers.ModelSerializer):
    languages_spoken=Languages_serializer(many=True)
    sports= Sports_serializer(many=True)
    class Meta:
        model=Student
        fields=['name','rollno','languages_spoken','sports']


class courseforStudent_serializer(serializers.ModelSerializer):
    #students=Student_serializer(many=True)
    class Meta:
        model=CourseforStudent
        fields=['name']


class Enrollement_serializer(serializers.ModelSerializer):
    course=courseforStudent_serializer()
    student=Student_serializer()

    class Meta:
        model=Enrollement
        fields=['id','date','completion','course','student']

    def create(self,validated_data):
        coursename=validated_data['course']['name']
        course_exists=CourseforStudent.objects.filter(name=coursename).exists()
        studentname=validated_data['student']['name']
        student_exists=Student.objects.filter(name=studentname).exists()
        if course_exists==True and student_exists==True:
            course=CourseforStudent.objects.get(name=coursename)
            student_now=Student.objects.get(name=studentname)
            Enrollment_obj=Enrollement.objects.create(course=course,student=student_now,date=validated_data['date'],completion=validated_data['completion'])
        elif course_exists==True and student_exists==False:
            student_now=Student.objects.create(name=studentname,rollno=validated_data['student']['rollno'])
            student_now.save()
            ###languages should be added first
            for languages in validated_data['student']['languages_spoken']:
                if Languages.objects.filter(name=languages['name']).exists():
                    lang_obj=Languages.objects.get(name=languages['name'])
                    student_now.languages_spoken.add(lang_obj)
                    student_now.save()
                else:
                    new_language =Languages.objects.create(name=languages['name'])
                    new_language.save()
                    student_now.languages_spoken.add(new_language)
                    student_now.save()


            ###sports
            for sports_iter in validated_data['student']['sports']:
                if Sports.objects.filter(sport_name=sports_iter['sport_name']).exists():
                    sport_obj=Sports.objects.get(sport_name=sports_iter['sport_name'])
                    student_now.sports.add(sport_obj)
                    student_now.save()
                else:
                    new_sport =Sports.objects.create(sport_name=sports_iter['sport_name'])
                    new_sport.save()
                    student_now.sports.add(new_sport)
                    student_now.save()

            course=CourseforStudent.objects.get(name=coursename)
            Enrollment_obj = Enrollement.objects.create(course=course, student=student_now, date=validated_data['date'],completion=validated_data['completion'])
        elif course_exists==False and student_exists==True:
            course=CourseforStudent.objects.create(name=coursename)
            student_now=Student.objects.get(name=studentname)
            Enrollment_obj = Enrollement.objects.create(course=course, student=student_now, date=validated_data['date'],completion=validated_data['completion'])
        else:
            ###first create student object
            student_now=Student.objects.create(name=studentname,rollno=validated_data['student']['rollno'])
            # student.save()
            ###languages should be added first
            for languages in validated_data['student']['languages_spoken']:
                if Languages.objects.filter(name=languages['name']).exists():
                    lang_obj=Languages.objects.get(name=languages['name'])
                    student_now.languages_spoken.add(lang_obj)
                    student_now.save()
                else:
                    new_language =Languages.objects.create(name=languages['name'])
                    new_language.save()
                    student_now.languages_spoken.add(new_language)
                    student_now.save()

            ###sports
            for sports_iter in validated_data['student']['sports']:
                if Sports.objects.filter(sport_name=sports_iter['sport_name']).exists():
                    sport_obj=Sports.objects.get(sport_name=sports_iter['sport_name'])
                    student_now.sports.add(sport_obj)
                    student_now.save()
                else:
                    new_sport = Sports.objects.create(sport_name=sports_iter['sport_name'])
                    new_sport.save()
                    student_now.sports.add(new_sport)
                    student_now.save()
            ### then create course object and add using enrollement
            course=CourseforStudent.objects.create(name=coursename)
            Enrollment_obj = Enrollement.objects.create(course=course, student=student_now, date=validated_data['date'],completion=validated_data['completion'])

        return Enrollment_obj
    #//////update method then

    def update(self, instance, validated_data):
        #print('printing student details',instance.student.name,instance.student.rollno)
        coursename=validated_data['course']['name']
        course_exists=CourseforStudent.objects.filter(name=coursename).exists()
        studentname=validated_data['student']['name']
        student_exists=Student.objects.filter(name=studentname).exists()
        if course_exists==True and student_exists==True:
            student_now = Student.objects.get(name=studentname)
            ###languages should be added first
            student_now.languages_spoken.clear()
            student_now.sports.clear()
            for languages in validated_data['student']['languages_spoken']:
                if Languages.objects.filter(name=languages['name']).exists():
                    lang_obj = Languages.objects.get(name=languages['name'])
                    student_now.languages_spoken.add(lang_obj)
                    student_now.save()
                else:
                    new_language = Languages.objects.create(name=languages['name'])
                    new_language.save()
                    student_now.languages_spoken.add(new_language)
                    student_now.save()

            ###sports
            for sports_iter in validated_data['student']['sports']:
                if Sports.objects.filter(sport_name=sports_iter['sport_name']).exists():
                    sport_obj = Sports.objects.get(sport_name=sports_iter['sport_name'])
                    student_now.sports.add(sport_obj)
                    student_now.save()
                else:
                    new_sport = Sports.objects.create(sport_name=sports_iter['sport_name'])
                    new_sport.save()
                    student_now.sports.add(new_sport)
                    student_now.save()

            course = CourseforStudent.objects.get(name=coursename)
            Enrollment_obj = Enrollement.objects.update_or_create(id=instance.id,defaults={'course':course,'student':student_now,'date':validated_data['date'],'completion':validated_data['completion']})
        elif course_exists==True and student_exists==False:
            student_now=Student.objects.get(name=instance.student.name)
            student_now.languages_spoken.clear()
            student_now.sports.clear()
            ###languages should be added first
            for languages in validated_data['student']['languages_spoken']:
                if Languages.objects.filter(name=languages['name']).exists():
                    lang_obj=Languages.objects.get(name=languages['name'])
                    student_now.languages_spoken.add(lang_obj)
                    student_now.save()
                else:
                    new_language =Languages.objects.create(name=languages['name'])
                    new_language.save()
                    student_now.languages_spoken.add(new_language)
                    student_now.save()


            ###sports
            for sports_iter in validated_data['student']['sports']:
                if Sports.objects.filter(sport_name=sports_iter['sport_name']).exists():
                    sport_obj=Sports.objects.get(sport_name=sports_iter['sport_name'])
                    student_now.sports.add(sport_obj)
                    student_now.save()
                else:
                    new_sport =Sports.objects.create(sport_name=sports_iter['sport_name'])
                    new_sport.save()
                    student_now.sports.add(new_sport)
                    student_now.save()
            student_now.name=validated_data['student']['name']
            student_now.save()
            student_now.rollno=validated_data['student']['rollno']
            student_now.save()
            #ere relationship exists but we are renaming student name
            course=CourseforStudent.objects.get(name=coursename)
            Enrollment_obj = Enrollement.objects.update_or_create(id=instance.id,defaults={'course':course,'student':student_now,'date':validated_data['date'],'completion':validated_data['completion']})
        elif course_exists==False and student_exists==True:
            #here relationship doesnot exists and we have to create new course and establish relatioship b/w newone and delete relation b/w oldone
            student_now = Student.objects.get(name=studentname)
            instance_course=CourseforStudent.objects.get(name=instance.course.name)
            instance_course.students.remove(student_now)
            instance_course.save()
            course=CourseforStudent.objects.create(name=coursename)
            Enrollment_obj = Enrollement.objects.update_or_create(id=instance.id,defaults={'course': course, 'student': student_now,'date': validated_data['date'],'completion': validated_data['completion']})
        else:
            #first create student object
            student_now=Student.objects.get(name=instance.student.name)
            # student.save()
            #languages should be added first
            student_now.languages_spoken.clear()
            student_now.sports.clear()
            for languages in validated_data['student']['languages_spoken']:
                if Languages.objects.filter(name=languages['name']).exists():
                    lang_obj=Languages.objects.get(name=languages['name'])
                    student_now.languages_spoken.add(lang_obj)
                    student_now.save()
                else:
                    new_language =Languages.objects.create(name=languages['name'])
                    new_language.save()
                    student_now.languages_spoken.add(new_language)
                    student_now.save()

            ###sports
            for sports_iter in validated_data['student']['sports']:
                if Sports.objects.filter(sport_name=sports_iter['sport_name']).exists():
                    sport_obj=Sports.objects.get(sport_name=sports_iter['sport_name'])
                    student_now.sports.add(sport_obj)
                    student_now.save()
                else:
                    new_sport = Sports.objects.create(sport_name=sports_iter['sport_name'])
                    new_sport.save()
                    student_now.sports.add(new_sport)
                    student_now.save()
            ### then create course object and add using enrollement
            instance_course=CourseforStudent.objects.get(name=instance.course.name) #firstgetting course and deleting relationship b/w course and student
            instance_course.students.remove(student_now)
            instance_course.save()
            course=CourseforStudent.objects.create(name=coursename)
            student_now.name=validated_data['student']['name']
            student_now.save()
            student_now.rollno=validated_data['student']['rollno']
            student_now.save()
            Enrollment_obj = Enrollement.objects.update_or_create(id=instance.id,defaults={'course': course, 'student': student_now,'date': validated_data['date'],'completion': validated_data['completion']})


        return Enrollment_obj







