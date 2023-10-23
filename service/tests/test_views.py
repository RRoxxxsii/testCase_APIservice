import json

from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from service.models import Employee, Store


class FixtureData:

    def setUp(self):
        fake = Faker()
        self.employee_name = fake.name()
        self.employee_name2 = fake.name()
        self.employee_name3 = fake.name()
        self.employee_name4 = fake.name()

        self.mobile = fake.unique.phone_number()
        self.mobile2 = fake.unique.phone_number()
        self.mobile3 = fake.unique.phone_number()
        self.mobile4 = fake.unique.phone_number()
        self.mobile5 = fake.unique.phone_number()

        self.latitude = fake.latitude()
        self.longitude = fake.longitude()

        self.employee = Employee.objects.create(user_name=self.employee_name, mobile=self.mobile)
        self.employee2 = Employee.objects.create(user_name=self.employee_name2, mobile=self.mobile2)
        self.employee4 = Employee.objects.create(user_name=self.employee_name3, mobile=self.mobile3)
        self.employee4 = Employee.objects.create(user_name=self.employee_name4, mobile=self.mobile4)

        self.store = Store.objects.create(name=fake.company(), user=self.employee)
        self.store2 = Store.objects.create(name=fake.company(), user=self.employee)
        self.store3 = Store.objects.create(name=fake.company(), user=self.employee)
        self.store4 = Store.objects.create(name=fake.company(), user=self.employee)
        self.store5 = Store.objects.create(name=fake.company(), user=self.employee)

        self.store7 = Store.objects.create(name=fake.company(), user=self.employee2)
        self.store8 = Store.objects.create(name=fake.company(), user=self.employee2)
        self.store9 = Store.objects.create(name=fake.company(), user=self.employee2)
        self.store10 = Store.objects.create(name=fake.company(), user=self.employee2)


class TestListStoreAPIView(FixtureData, APITestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('store-list')

    def test_get_list_but_not_mobile(self):
        """
        Номер мобильного телефона не указан.
        """
        response = self.client.post(self.url,)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_list_but_mobile_not_correct(self):
        """
        Номер мобильного телефона не принадлежит ни одному из пользователей.
        """
        response = self.client.post(self.url, data={'mobile': self.mobile5})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_list_status_code(self):
        """
        Все условия удовлетворены. Тестируем код ответа.
        """
        response = self.client.post(self.url, data={'mobile': self.mobile})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_data(self):
        """
        Все условия удовлетворены. Тестируем полученные данные.
        """
        response = self.client.post(self.url, data={'mobile': self.mobile})
        content = json.loads(response.content.decode())
        self.assertEqual(len(content), 5)
        self.assertEqual(len(content[0]), 2)
        self.assertIn('id', content[0])
        self.assertIn('name', content[0])


class TestVisitStoreAPIView(FixtureData, APITestCase):

    def setUp(self):
        super().setUp()
        self.url = reverse('create-visit')

    def test_create_but_not_mobile(self):
        """
        Номер мобильного телефона не указан.
        """
        response = self.client.post(self.url, data={'latitude': self.latitude,
                                                    'longitude': self.longitude,
                                                    'store_id': self.store.pk})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_but_mobile_not_correct(self):
        """
        Номер мобильного телефона не принадлежит ни одному из пользователей.
        """
        response = self.client.post(self.url, data={'mobile': self.mobile5,
                                                    'latitude': self.latitude,
                                                    'longitude': self.longitude,
                                                    'store_id': self.store.pk})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_status_code(self):
        """
        Код ответа при создании. Номер привязан к торговой точке.
        """
        response = self.client.post(self.url, data={'mobile': self.mobile,
                                                    'latitude': self.latitude,
                                                    'longitude': self.longitude,
                                                    'store_id': self.store.pk})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_number_not_linked_status_code(self):
        """
        Код ответа при создании. Номер не привязан к торговой точке.
        """
        response = self.client.post(self.url, data={'mobile': self.mobile,
                                                    'latitude': self.latitude,
                                                    'longitude': self.longitude,
                                                    'store_id': self.store7.pk})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_data(self):
        """
        Содержимое ответа. Номер привязан к торговой точке.
        """
        response = self.client.post(self.url, data={'mobile': self.mobile,
                                                    'latitude': self.latitude,
                                                    'longitude': self.longitude,
                                                    'store_id': self.store.pk})
        content = json.loads(response.content.decode())
        self.assertIn('id', content)
        self.assertIn('datetime_visited', content)
