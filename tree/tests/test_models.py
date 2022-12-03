from django.test import TestCase

from django.utils.translation import gettext_lazy as _

import datetime
from django.utils import timezone

# Create your tests here.
# Подключение моделей
from ..models import Person, PersonList
from django.contrib.auth.models import User


# Тестирует значение параметра для всех объектов модели
def run_field_parameter_test(
        model, self_,
        field_and_parameter_value: dict,
        parameter_name: str) -> None:
    # Вначале мы получаем все объекты модели и проходимся по ним.
    # Дальше обходим словарь с полями и ожидаемыми значениями параметров.
    # После получаем реальные значения параметров, обращаясь к объекту.
    # А затем сравниваем их с ожидаемыми.
    for instance in model.objects.all():
        # Пример 1: field = "email"; expected_value = 256.
        # Пример 2: field = "email"; expected_value = "Электронная почта".
        for field, expected_value in field_and_parameter_value.items():
            parameter_real_value = getattr(
                instance._meta.get_field(field), parameter_name
            )
            self_.assertEqual(parameter_real_value, expected_value)

# Миксин для проверки verbose_name
# Мы создаём нужный метод и в нём вызываем нашу общую функцию с соответствующими параметрами.
# self.field_and_verbose_name и self.field_and_max_length берутся из класса, который наследуется от миксина.
# А именно – из метода setUpTestData класса OrganizationTests.
class TestVerboseNameMixin:
    # Метод, тестирующий verbose_name
    def run_verbose_name_test(self, model):
        run_field_parameter_test(
            model, self, self.field_and_verbose_name, 'verbose_name'
        )

# Миксин для проверки max_length
class TestMaxLengthMixin:
    def run_max_length_test(self, model):
        # Метод, тестирующий max_length
        run_field_parameter_test(
            model, self, self.field_and_max_length, 'max_length'
        )

########### Проверка моделей ###########
        
# Наследуем класс CategoryModelTest от наших миксинов.
class PersonModelTest(TestCase, TestVerboseNameMixin, TestMaxLengthMixin):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        person = Person.objects.create(surname='surname', 
                                       name='name', 
                                       patronymic='patronymic', 
                                       sex='M', 
                                       birthday=timezone.now(),
                                       tribe='tribe',
                                       clan='clan',
                                       phone='phone',
                                       address='address',
                                       email='email',
                                       photo=None,
                                       details='details',
                                       father=None,
                                       mother=None)
        person.save()
        cls.field_and_verbose_name = {
            'surname': _('surname'),            
            'name': _('name'),            
            'patronymic': _('patronymic'),            
            'birthday': _('birthday'),            
            'tribe': _('tribe'),            
            'clan': _('clan'),            
            'phone': _('phone'),            
            'address': _('address'),            
            'email': _('email'),            
            'photo': _('photo'),            
            'details': _('details'),            
        }
        cls.field_and_max_length = {
            'surname': 64,
            'name': 64,
            'patronymic': 64,
            'sex': 1,
            'tribe': 256,
            'clan': 256,
            'phone': 128,
            'address': 128,
            'email': 128,
        }
    # Тест параметра verbose_name
    def test_verbose_name(self):        
        super().run_verbose_name_test(Person)
    # Тест параметра max_length
    def test_max_length(self):        
        super().run_max_length_test(Person)
        
