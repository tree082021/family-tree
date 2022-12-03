from django.db import models
from django.utils.translation import gettext_lazy as _

from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from django.core.files.storage import default_storage as storage  

# Модели отображают информацию о данных, с которыми вы работаете.
# Они содержат поля и поведение ваших данных.
# Обычно одна модель представляет одну таблицу в базе данных.
# Каждая модель это класс унаследованный от django.db.models.Model.
# Атрибут модели представляет поле в базе данных.
# Django предоставляет автоматически созданное API для доступа к данным


# choices (список выбора). Итератор (например, список или кортеж) 2-х элементных кортежей,
# определяющих варианты значений для поля.
# При определении, виджет формы использует select вместо стандартного текстового поля
# и ограничит значение поля указанными значениями.

# Человек 
class Person(models.Model):
    # Читабельное имя поля (метка, label). Каждое поле, кроме ForeignKey, ManyToManyField и OneToOneField,
    # первым аргументом принимает необязательное читабельное название.
    # Если оно не указано, Django самостоятельно создаст его, используя название поля, заменяя подчеркивание на пробел.
    # null - Если True, Django сохранит пустое значение как NULL в базе данных. По умолчанию - False.
    # blank - Если True, поле не обязательно и может быть пустым. По умолчанию - False.
    # Это не то же что и null. null относится к базе данных, blank - к проверке данных.
    # Если поле содержит blank=True, форма позволит передать пустое значение.
    # При blank=False - поле обязательно.
    SEX_CHOICES = (
        ('М','М'),
        ('Ж', 'Ж'),
    )
    surname = models.CharField(_('surname'), max_length=64)
    name = models.CharField(_('name'), max_length=64)
    patronymic = models.CharField(_('patronymic'), max_length=64, blank=True, null=True)    
    sex = models.CharField(_('sex'), max_length=1, choices=SEX_CHOICES, default='М')
    birthday = models.DateTimeField(_('birthday'))
    tribe = models.CharField(_('tribe'), max_length=256, blank=True, null=True)
    clan = models.CharField(_('clan'), max_length=256, blank=True, null=True)
    phone = models.CharField(_('phone'), max_length=128, blank=True, null=True)
    address = models.CharField(_('address'), max_length=128, blank=True, null=True)
    email = models.CharField(_('email'), max_length=128, blank=True, null=True)
    photo = models.ImageField(_('photo'), upload_to='images/', blank=True, null=True)
    details = models.TextField(_('details'), blank=True, null=True)
    father = models.ForeignKey('self', blank=True, null=True, related_name='person_father', on_delete=models.CASCADE)
    mother = models.ForeignKey('self', blank=True, null=True, related_name='mother_father', on_delete=models.CASCADE)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'person'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['surname']),
            models.Index(fields=['name']),
            models.Index(fields=['patronymic']),
        ]
        # Сортировка по умолчанию
        ordering = ['surname', 'name', 'patronymic']
    def __str__(self):
        # Вывод ФИО в тег SELECT 
        return "{} {} {}".format(self.surname, self.name, self.patronymic)
        # Override the save method of the model
    #def save(self):
    #    super().save()
    #    img = Image.open(self.photo.path) # Open image
    #    if img is not None:
    #        # resize image
    #        if img.width > 512 or img.height > 700:
    #            proportion_w_h = img.width/img.height  # Отношение ширины к высоте 
    #            output_size = (512, int(512/proportion_w_h))
    #            img.thumbnail(output_size) # Изменение размера
    #            img.save(self.photo.path) # Сохранение
    #def save(self):
    #    super().save()
    #    img = Image.open(self.photo.path) # Open image
    #    # resize image
    #    if img.width > 512 or img.height > 512:
    #        proportion_w_h = img.width/img.height  # Отношение ширины к высоте 
    #        output_size = (512, int(512/proportion_w_h))
    #        img.thumbnail(output_size) # Изменение размера
    #        img.save(self.photo.path) # Сохранение
    @property
    def fio(self):
        # Возврат ФИО
        return '%s %s %s' % (self.surname, self.name, self.patronymic)
    @property
    def ru(self):
        # Возврат Ру
        return '%s, %s' % (self.tribe, self.clan)

# Человек 
class PersonList(models.Model):
    # CREATE VIEW person_list AS SELECT id, surname || ' ' || name  || ' ' || patronymic AS fio, sex, birthday, tribe, clan, phone, address, email, photo, details, father_id, (SELECT surname || ' ' || name || ' ' || patronymic FROM Person f WHERE f.id=p.father_id) AS father, mother_id, (SELECT surname || ' ' || name || ' ' || patronymic FROM Person m WHERE m.id=p.mother_id) AS mother, (SELECT GROUP_CONCAT(surname || ' ' || name || ' ' || patronymic,'; ') FROM Person c WHERE c.father_id=p.id ORDER BY birthday) AS children FROM Person p
    # SQLite:
    # CREATE VIEW person_list AS SELECT id, iif( surname = "Нет данных", "", surname || ' ')  || name  || iif(patronymic NOT Null, ' '  || patronymic, '') AS fio, sex, birthday, iif(strftime('%Y',birthday)>"1900", strftime('%d.%m.%Y',birthday),"") AS birthday20, tribe, clan, phone, address, email, photo, details, father_id, (SELECT iif( surname = "Нет данных", "", surname || ' ')  || name || iif(patronymic NOT Null, ' '  || patronymic, '')  FROM Person f WHERE f.id=p.father_id) AS father, mother_id, (SELECT iif( surname = "Нет данных", "", surname || ' ')  || name || iif(patronymic NOT Null, ' '  || patronymic, '')  FROM Person m WHERE m.id=p.mother_id) AS mother, (SELECT GROUP_CONCAT(name ||  iif(strftime('%Y',birthday)>"1900", ' (' || strftime('%Y',birthday) || ')',"") ,'; ') FROM Person c WHERE c.father_id=p.id ORDER BY birthday) AS children FROM Person p
    # PostgreSQL
    """
    CREATE VIEW person_list AS 
    SELECT id, 
	CASE WHEN surname = 'Нет данных' THEN name 
		ELSE surname || ' '  || name  
		|| 
	CASE WHEN patronymic IS Null THEN ''  
		ELSE ' ' || patronymic
	END
	END
	AS fio, 
sex, birthday, 
	CASE WHEN EXTRACT(YEAR FROM birthday) >1900 THEN to_char( birthday, 'DD-MM-YYYY')
	ELSE ''
	END
	AS birthday20, 
tribe, clan, phone, address, email, photo, details, father_id, 
(SELECT 
 	CASE WHEN surname = 'Нет данных' THEN name
 	ELSE surname || ' ' || name || 
 	CASE WHEN patronymic IS Null THEN ''  
 	ELSE ' ' || patronymic
 	END
 	END 
 FROM Person f WHERE f.id=p.father_id) AS father, mother_id, 
 (SELECT 
 	CASE WHEN surname = 'Нет данных' THEN name
 	ELSE surname || ' ' || name || 
 	CASE WHEN patronymic IS Null THEN ''  
 	ELSE ' ' || patronymic
 	END
 	END 
 FROM Person f WHERE f.id=p.mother_id) AS mother, 
  (SELECT array_agg(name ||  
	CASE WHEN EXTRACT(YEAR FROM birthday) >1900 THEN ' (' || to_char( birthday, 'YYYY') || ')'
	ELSE ''
	END
    ) FROM Person c WHERE c.father_id=p.id) AS children FROM Person p
    """
    SEX_CHOICES = (
        ('М','М'),
        ('Ж', 'Ж'),
    )
    fio = models.CharField(_('fio'), max_length=192)
    sex = models.CharField(_('sex'), max_length=1, choices=SEX_CHOICES, default='М')
    birthday = models.DateTimeField(_('birthday'))
    birthday20 = models.CharField(_('birthday'), max_length=20)
    tribe = models.CharField(_('tribe'), max_length=256, blank=True, null=True)
    clan = models.CharField(_('clan'), max_length=256, blank=True, null=True)
    phone = models.CharField(_('phone'), max_length=128, blank=True, null=True)
    address = models.CharField(_('address'), max_length=128, blank=True, null=True)
    email = models.CharField(_('email'), max_length=128, blank=True, null=True)
    photo = models.ImageField(_('photo'), upload_to='images/', blank=True, null=True)
    details = models.TextField(_('details'), blank=True, null=True)
    father_id = models.IntegerField()
    father = models.CharField(_('father'), max_length=192)
    mother_id = models.IntegerField()
    mother = models.CharField(_('mother'), max_length=192)
    children = models.TextField(_('children'), blank=True, null=True)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'person_list'
        # Сортировка по умолчанию
        ordering = ['fio']
        # Таблицу не надо не добавлять не удалять
        managed = False
