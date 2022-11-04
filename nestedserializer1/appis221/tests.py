import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .models import Books_model
from .serializers import *
from .models import *

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data={"name":"wisdom of life","price":250}
        url="/api/testing_book_view"
        response=self.client.post(url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

class Authuser(APITestCase):
    # list_url=reverse("authusertesting-list")
    # def setUp(self):
    #     self.user=User.objects.create_user(username='vijju',password='vijju@123')
    #     self.token=Token.objects.create(user=self.user)
    #     self.api_authentication
    #
    # def api_authentication(self):
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    #
    # def test_profile_list_authenticated(self):
    #     response=self.client.get(self.list_url)
    #     self.assertEqual(response.status_code,status.HTTP_200_OK)
    #
    # def test_profile_list_un_authenticated(self):
    #     self.client.force_authentication(user=None)
    #     response=self.client.get(self.list_url)
    #     self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
    #
    # def test_profile_detail_retrieve(self):
    #     response=self.client.get(reverse("authusertesting-detail",kwargs={'pk':1}))
    #     self.assertEqual(response.status_code,status.HTTP_200_OK)
    #     self.assertEqual(response.data['user'],'vijju')
    def setUp(self):
        user=User.objects.create(username='vijju',email='vijjucse@gmail.com')
        user.set_password('vijju@123')
        user.save()

    def test_creating_status(self):
        user=User.objects.get(username='vijju')
        cnt=Authmodel.objects.all().count()
        obj=Authmodel.objects.create(user=user,study="eamtech from iit")
        self.assertEqual(obj.id,1)
        qs=Authmodel.objects.all().count()
        self.assertEqual(qs,cnt+1)

    def test_register_user_api_fail(self):
        url = reverse('user-detail')
        data={

        'username':'sanju',
        'email':'sanju@gmail.com',
        'password':'sanju@123',

        }
        response=self.client.post(url,data,format='json')
        print(response.data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

        #self.assertEqual((response.data['password2'][0],'This field is required.'))

    def test_register_user_api(self):
        url = reverse('user-detail')
        data = {

            'username': 'sanju',
            'email': 'sanju@gmail.com',
            'password': 'sanju@123',

        }
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        token_len = len(response.data.get('token', 0))
        self.assertGreater((token_len,0))
        # self.assertEqual((response.data['password2'][0],'This field is required.'))