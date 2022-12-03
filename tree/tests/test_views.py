from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.test import Client

from ..models import Person

from django.contrib.auth.models import User, Group

import datetime
from django.utils import timezone
       
class PersonViewTest(TestCase):
    def setUp(self):
        # Создание пользователя
        test_user1 = User.objects.create_user(username='testuser1', password='Tt12345+')
        test_user1.save()
        # Группа менеджеров уже создана при миграции
        managers = Group.objects.get(name='Managers')
        # Пользователь с ролью менеджера 
        managers.user_set.add(test_user1)
    def test_logged_in_uses_correct_template(self):
        # Вход пользователя
        login = self.client.login(username='testuser1', password='Tt12345+')
        # Переход на указанную страницу (представление)
        resp = self.client.get(reverse('person_index'))
        # Проверка что пользователь залогинился
        self.assertEqual(str(resp.context['user']), 'testuser1')
        # Проверка ответа на запрос
        self.assertEqual(resp.status_code, 200)
        # Проверка того, что мы используем правильный шаблон
        self.assertTemplateUsed(resp, 'person/index.html')
    # Проверка представление для неаутентифицированного пользователя,
    # если пользователь неавторизованный - перенаправит на страницу входа
    # LOGIN_REDIRECT_URL = '/', LOGIN_URL = '/login/'
    def test_view_deny_anonymous(self):
        response = self.client.get('/person/index/')
        self.assertRedirects(response, '/login/?next=/person/index/')             
        response = self.client.post('/person/index/')
        self.assertRedirects(response, '/login/?next=/person/index/')
    # Проверка POST-запроса, GET-запроса
    def test_view_post(self):
        # Добавляемые в запросе данные        
        data = {"surname": "Иванов", 
                "name": "Иван", 
                "patronymic": "Иванович",
                "sex": "М",
                "birthday": timezone.now(),
                "tribe": "Арғын",
                "clan": "Қанжығалы",
                "phone": "+7-701-111-2222",
                "address": "ул. Ленина, 6-12",
                "email": "email@mail.ru",
                "details": ""} 
        # Залогиниться
        login = self.client.login(username='testuser1', password='Tt12345+')
        # Отправить POST-запрос присваивание follow=True, в запросе, гарантирует что запрос вернёт окончательный URL-адрес пункта назначения (следовательно проверяется /catalog/, а не /)
        response = self.client.post(reverse('person_create'), data, follow=True)
        # Проверить возврат на страницу index после успешного сохранения
        self.assertRedirects(response, '/person/index/')        
        self.assertEqual( response.status_code, 200)
        # Получить id последнего добавленного объекта
        latest_obj = Person.objects.latest('id')
        #print("latest obj id ", latest_obj.id)
        # Получить страницу с добавленным объектом
        response = self.client.get(reverse('person_read', kwargs={'id': latest_obj.id,}))
        self.assertEqual(response.status_code, 200)
        

