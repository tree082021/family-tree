from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import migrations

def new_person(apps, schema_editor):
    
    user = User.objects.create_superuser(username='mabylmazhitov',
        email='mabylmazhitov@gmail.com',
        password='Mm100Ff+Tt-*789')
    managers = Group.objects.get_or_create(name = 'Managers')
    my_group = Group.objects.get(name='Managers')    
    my_group.user_set.add(user)
    managers = Group.objects.get_or_create(name = 'Readers')

    Person = apps.get_model("tree", "Person")
   
    ##### Легенды #####
    
    person = Person()
    person.id = 1
    person.surname = 'Нет данных'
    person.name = 'Ақжол'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1690-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'    
    person.save()

    person = Person()
    person.id = 2
    person.surname = 'Нет данных'
    person.name = 'Қаракожа'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1700-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 1
    person.save()

    person = Person()
    person.id = 3
    person.surname = 'Нет данных'
    person.name = 'Кенжесопы'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1710-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 2
    person.save()

    person = Person()
    person.id = 4
    person.surname = 'Нет данных'
    person.name = 'Ақсопы'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1710-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 2
    person.details = 'балалары Момын токаложан'
    person.save()

    person = Person()
    person.id = 5
    person.surname = 'Нет данных'
    person.name = 'Қанжығалы (Толыбай)'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1720-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 4
    person.save()

    person = Person()
    person.id = 6
    person.surname = 'Нет данных'
    person.name = 'Тобықты'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1720-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 4
    person.save()

    person = Person()
    person.id = 7
    person.surname = 'Нет данных'
    person.name = 'Jшпек'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1730-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 5
    person.save()

    person = Person()
    person.id = 8
    person.surname = 'Нет данных'
    person.name = 'Піспекбай'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1730-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 5
    person.details = 'ұлы жоқ қызынан Қуандықтын ар Алтайы өрбіген'
    person.save()

    person = Person()
    person.id = 9
    person.surname = 'Нет данных'
    person.name = 'Есен'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1740-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 7
    person.save()

    person = Person()
    person.id = 10
    person.surname = 'Нет данных'
    person.name = 'Бозым'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1740-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 7
    person.save()

    person = Person()
    person.id = 11
    person.surname = 'Нет данных'
    person.name = 'Қармыс'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1750-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 9
    person.save()

    person = Person()
    person.id = 12
    person.surname = 'Нет данных'
    person.name = 'Қамбар'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1750-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 9
    person.save()

    person = Person()
    person.id = 13
    person.surname = 'Нет данных'
    person.name = 'Жанар'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1750-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 9
    person.save()

    person = Person()
    person.id = 14
    person.surname = 'Нет данных'
    person.name = 'Әжібай'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1760-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 11
    person.save()

    person = Person()
    person.id = 15
    person.surname = 'Нет данных'
    person.name = 'Әжім'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1760-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 11
    person.save()

    person = Person()
    person.id = 16
    person.surname = 'Нет данных'
    person.name = 'Әжіқұл'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1760-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 11
    person.save()

    person = Person()
    person.id = 17
    person.surname = 'Нет данных'
    person.name = 'Машен'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1770-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 14
    person.save()

    person = Person()
    person.id = 18
    person.surname = 'Нет данных'
    person.name = 'Жарас'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1770-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 14
    person.save()

    person = Person()
    person.id = 19
    person.surname = 'Нет данных'
    person.name = 'Мамбетқазы'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1770-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 14
    person.save()

    person = Person()
    person.id = 20
    person.surname = 'Нет данных'
    person.name = 'Мамбетқұл'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1770-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 14
    person.save()

    person = Person()
    person.id = 21
    person.surname = 'Нет данных'
    person.name = 'Ақтамақ'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1770-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 14
    person.save()

    person = Person()
    person.id = 22
    person.surname = 'Нет данных'
    person.name = 'Ақбура'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1770-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 14
    person.save()
    
    person = Person()
    person.id = 23
    person.surname = 'Нет данных'
    person.name = 'Кара'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1780-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 17
    person.save()

    person = Person()
    person.id = 24
    person.surname = 'Нет данных'
    person.name = 'Сары'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1790-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 23
    person.save()

    person = Person()
    person.id = 25
    person.surname = 'Нет данных'
    person.name = 'Елібай'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1790-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 23
    person.save()

    person = Person()
    person.id = 26
    person.surname = 'Нет данных'
    person.name = 'Жәдігер'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1790-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 23
    person.save()

    person = Person()
    person.id = 27
    person.surname = 'Нет данных'
    person.name = 'Жылкелді'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1810-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 24
    person.save()

    person = Person()
    person.id = 28
    person.surname = 'Нет данных'
    person.name = 'Қойбас'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1810-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 24
    person.save()

    person = Person()
    person.id = 29
    person.surname = 'Нет данных'
    person.name = 'Айбас'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1810-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 24
    person.save()

    person = Person()
    person.id = 30
    person.surname = 'Нет данных'
    person.name = 'Ақжігіт'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1820-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 27
    person.save()
    
    person = Person()
    person.id = 31
    person.surname = 'Нет данных'
    person.name = 'Шақар'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1820-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 27
    person.save()

    person = Person()
    person.id = 32
    person.surname = 'Нет данных'
    person.name = 'Шабаң'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1820-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 27
    person.save()

    person = Person()
    person.id = 33
    person.surname = 'Нет данных'
    person.name = 'Салкаң'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1820-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 27
    person.save()

    person = Person()
    person.id = 34
    person.surname = 'Нет данных'
    person.name = 'Томан'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1830-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 30
    person.save()
    
    person = Person()
    person.id = 35
    person.surname = 'Нет данных'
    person.name = 'Кулен'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1840-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 34
    person.save()

    person = Person()
    person.id = 36
    person.surname = 'Нет данных'
    person.name = 'Исамбай (Исенбай)'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1850-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 35
    person.save()

    person = Person()
    person.id = 37
    person.surname = 'Нет данных'
    person.name = 'Қожан'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1850-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 35
    person.save()

    person = Person()
    person.id = 38
    person.surname = 'Нет данных'
    person.name = 'Мустафа'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1850-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 35
    person.details = 'ұрпақ жоқ'
    person.save()
	
    person = Person()
    person.id = 39
    person.surname = 'Нет данных'
    person.name = 'Әмірхан'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1860-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 36
    person.save()
	
    person = Person()
    person.id = 40
    person.surname = 'Нет данных'
    person.name = 'Шөкір'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1860-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 36
    person.save()
	
    person = Person()
    person.id = 41
    person.surname = 'Нет данных'
    person.name = 'Мешітбай'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1860-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 36
    person.save()
	
    person = Person()
    person.id = 42
    person.surname = 'Нет данных'
    person.name = 'Қаржау'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1870-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 39
    person.save()
	
    person = Person()
    person.id = 43
    person.surname = 'Нет данных'
    person.name = 'Улбісін'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1880-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 42
    person.save()

    ##########
    
    person = Person()
    person.id = 44
    person.surname = 'Нет данных'
    person.name = 'Қуат'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1890-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 43
    person.save()

    ##########

    person = Person()
    person.id = 45
    person.surname = 'Куватов'
    person.name = 'Әбілқасым'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1911-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 44
    person.save()

    person = Person()
    person.id = 46
    person.surname = 'Куватов'
    person.name = 'Әбілмәжiт'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1914-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 44
    person.save()

    person = Person()
    person.id = 47
    person.surname = 'Куватов'
    person.name = 'Жылқыбай'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1917-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 44
    person.save()

    person = Person()
    person.id = 48
    person.surname = 'Куватов'
    person.name = 'Малғаждар'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1927-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 44
    person.save()

    ##########

    person = Person()
    person.id = 49
    person.surname = 'Куватов'
    person.name = 'Борис'
    person.patronymic = 'Абылмажитович'
    person.sex = 'М'
    person.birthday = '1940-01-26 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 46
    person.save()

    person = Person()
    person.id = 50
    person.surname = 'Есимжанова'
    person.name = 'Кулбаш'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1943-07-27 12:00:00'
    person.tribe = 'Найман'
    person.clan = 'Актiлес'
    person.father_id = 147
    person.mother_id = 148
    person.save()
    
    person = Person()
    person.id = 51
    person.surname = 'Конакбаев'
    person.name = 'Балтабек'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1938-11-06 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()
    
    person = Person()
    person.id = 52
    person.surname = 'Конакбаева'
    person.name = 'Мария'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1940-11-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 53
    person.surname = 'Әбілмәжiт'
    person.name = 'Мүрат'
    person.patronymic = 'Борісұлы'
    person.sex = 'М'
    person.birthday = '1967-10-24 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-775-237-0484, +7-705-254-5097'
    person.address = 'г. Павлодар, ул. Набережная, 5-61'
    person.email = 'mawoka67@gmail.com'
    person.father_id = 49
    person.mother_id = 50
    person.save()

    person = Person()
    person.id = 54
    person.surname = 'Абылмажитов'
    person.name = 'Марат'
    person.patronymic = 'Борисович'
    person.sex = 'М'
    person.birthday = '1969-12-28 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-701-914-4539'
    person.address = 'г. Павлодар, ул. Лермонтова, 44-118'
    person.email = 'MAbylmazhitov@gmail.com'
    person.father_id = 49
    person.mother_id = 50
    person.save()

    person = Person()
    person.id = 55
    person.surname = 'Конакбаева'
    person.name = 'Гаухар'
    person.patronymic = 'Балтабековна'
    person.sex = 'Ж'
    person.birthday = '1969-04-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.phone = '+7-701-914-4536'
    person.address = 'г. Павлодар, ул. Лермонтова, 44-118'
    person.email = 'users324581@gmail.com'
    person.father_id = 51
    person.mother_id = 52
    person.save()

    person = Person()
    person.id = 56
    person.surname = 'Абилмажит'
    person.name = 'Акмарал'
    person.patronymic = 'Мараткызы'
    person.sex = 'Ж'
    person.birthday = '1996-06-21 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-999-207-4865'
    person.address = 'г. Санкт-Петербург, ул.Кременчугская, д.11, к.2, кв.134'
    person.email = 'rei.kasano@gmail.com'
    person.father_id = 54
    person.mother_id = 55
    person.save()
    
    person = Person()
    person.id = 57
    person.surname = 'Әбілмәжит'
    person.name = 'Шынар'
    person.patronymic = 'Маратқызы'
    person.sex = 'Ж'
    person.birthday = '2004-05-03 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-701-914-4537'
    person.address = 'г. Павлодар, ул. Лермонтова, 44-118'
    person.email = 'user538542@gmail.com'
    person.father_id = 54
    person.mother_id = 55
    person.save()

    person = Person()
    person.id = 58
    person.surname = 'Куватова'
    person.name = 'Мадина'
    person.patronymic = 'Борискызы'
    person.sex = 'Ж'
    person.birthday = '1980-11-11 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-701-985-2780, +7-705-564-9056'
    person.address = 'г. Павлодар, ул. Набережная, 5-61'
    person.email = 'Kuvatova.madina@gmail.com'
    person.father_id = 49
    person.mother_id = 50
    person.save()

    ##########
    
    person = Person()
    person.id = 59
    person.surname = 'Куватов'
    person.name = 'Бари'
    person.patronymic = 'Абылмажитович'
    person.sex = 'М'
    person.birthday = '1942-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-705-162-1487'    
    person.father_id = 46
    person.save()

    person = Person()
    person.id = 60
    person.surname = 'Куватова'
    person.name = 'Даметкен'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1942-01-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 61
    person.surname = 'Карагужинова'
    person.name = 'Жанар'
    person.patronymic = 'Бариқызы'
    person.sex = 'Ж'
    person.birthday = '1968-07-22 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 59
    person.mother_id = 60
    person.phone = '+7-702-538-0813'
    person.save()

    person = Person()
    person.id = 62
    person.surname = 'Карагужинов'
    person.name = 'Марат'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1968-07-22 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.phone = '+7-701-670-2880'
    person.save()

    person = Person()
    person.id = 63
    person.surname = 'Карагужинова'
    person.name = 'Асем'
    person.patronymic = 'Маратқызы'
    person.sex = 'Ж'
    person.birthday = '1989-01-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.father_id = 62
    person.mother_id = 61
    person.save()

    person = Person()
    person.id = 64
    person.surname = 'Карагужинова'
    person.name = 'Асель'
    person.patronymic = 'Маратқызы'
    person.sex = 'Ж'
    person.birthday = '1990-01-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.father_id = 62
    person.mother_id = 61
    person.save()

    person = Person()
    person.id = 65
    person.surname = 'Карагужинова'
    person.name = 'Айсара'
    person.patronymic = 'Маратқызы'
    person.sex = 'Ж'
    person.birthday = '2008-01-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.father_id = 62
    person.mother_id = 61
    person.save()

    person = Person()
    person.id = 66
    person.surname = 'Абылмажитова'
    person.name = 'Анар'
    person.patronymic = 'Бариқызы'
    person.sex = 'Ж'
    person.birthday = '1970-01-09 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-776-266-5126'
    person.address = 'г. Павлодар, ул. Ак. Чокина, 24-151'    
    person.father_id = 59
    person.mother_id = 60
    person.save()

    person = Person()
    person.id = 67
    person.surname = 'Толеубаева'
    person.name = 'Асемгуль'
    person.patronymic = 'Бариқызы'
    person.sex = 'Ж'
    person.birthday = '1972-04-10 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-771-357-9970'
    person.details = 'муж Ардак, дети Алишер (1993 г.р.), Анел (2002 г.р.)'    
    person.father_id = 59
    person.mother_id = 60
    person.save()

    person = Person()
    person.id = 68
    person.surname = 'Куватова'
    person.name = 'Назгуль'
    person.patronymic = 'Бариқызы'
    person.sex = 'Ж'
    person.birthday = '1974-07-20 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-702-215-8239'
    person.details = 'муж Нуржан, Дарина (2002 г.р.), Эмир (2004 г.р.)'
    person.father_id = 59
    person.mother_id = 60
    person.save()

    person = Person()
    person.id = 69
    person.surname = 'Абылмажитова'
    person.name = 'Бибигуль'
    person.patronymic = 'Бариқызы'
    person.sex = 'Ж'
    person.birthday = '1976-04-28 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-775-186-2721'
    person.father_id = 59
    person.mother_id = 60
    person.save()

    person = Person()
    person.id = 70
    person.surname = 'Куватов'
    person.name = 'Бауыржан'
    person.patronymic = 'Бариұлы'
    person.sex = 'М'
    person.birthday = '1977-08-08 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-705-444-4110'
    person.father_id = 59
    person.mother_id = 60    
    person.save()

    person = Person()
    person.id = 71
    person.surname = 'Куватова'
    person.name = 'Сандугаш'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1977-08-08 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 72
    person.surname = 'Хасанова'
    person.name = 'Сауле'
    person.patronymic = 'Бариқызы'
    person.sex = 'Ж'
    person.birthday = '1979-11-02 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-705-151-2304'
    person.details = 'муж Ренат, дети Рустем (2003 г.р.), Ильяс (2011 г.р.)'
    person.father_id = 59
    person.mother_id = 60
    person.save()

    ##########
    
    person = Person()
    person.id = 73
    person.surname = 'Куватов'
    person.name = 'Мөжен'
    person.patronymic = 'Абылкасимович'
    person.sex = 'М'
    person.birthday = '1938-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 45
    person.save()

    person = Person()
    person.id = 74
    person.surname = 'Куватова'
    person.name = 'Жанар'
    person.patronymic = 'Мөженқызы'
    person.sex = 'Ж'
    person.birthday = '1962-01-25 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-705-612-8733'
    person.father_id = 73
    person.save()

    person = Person()
    person.id = 75
    person.surname = 'Куватова'
    person.name = 'Алма'
    person.patronymic = 'Мөженқызы'
    person.sex = 'Ж'
    person.birthday = '1964-02-25 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-705-165-6380'    
    person.details = 'муж Багиден Ахметов'
    person.father_id = 73
    person.save()

    ##########
    
    person = Person()
    person.id = 76
    person.surname = 'Куватов'
    person.name = 'Жасқайрат'
    person.patronymic = 'Абылкасимович'
    person.sex = 'М'
    person.birthday = '1939-04-04 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 45
    person.save()

    person = Person()
    person.id = 77
    person.surname = 'Куватова'
    person.name = 'Светлана'
    person.patronymic = 'Абылкасимовна'
    person.sex = 'Ж'
    person.birthday = '1946-03-24 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 45
    person.save()
    
    person = Person()
    person.id = 78
    person.surname = 'Куватов'
    person.name = 'Мурат'
    person.patronymic = 'Абылкасимович'
    person.sex = 'М'
    person.birthday = '1949-05-17 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-771-560-8405'
    person.father_id = 45
    person.save()

    person = Person()
    person.id = 79
    person.surname = 'Куватова'
    person.name = 'Азина'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1949-05-17 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    ##########
    
    person = Person()
    person.id = 80
    person.surname = 'Куватов'
    person.name = 'Булат'
    person.patronymic = 'Абылкасимович'
    person.sex = 'М'
    person.birthday = '1954-06-30 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-701-551-7943'
    person.father_id = 45
    person.save()

    person = Person()
    person.id = 81
    person.surname = 'Куватова'
    person.name = 'Роза'
    person.patronymic = 'Абылкасимовна'
    person.sex = 'Ж'
    person.birthday = '1956-01-29 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-771-831-9587'
    person.father_id = 45
    person.save()

    person = Person()
    person.id = 82
    person.surname = 'Куватова'
    person.name = 'Сауле'
    person.patronymic = 'Абылкасимовна'
    person.sex = 'Ж'
    person.birthday = '1956-01-29 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-771-276-5010'
    person.father_id = 45
    person.save()

    person = Person()
    person.id = 83
    person.surname = 'Байзакова'
    person.name = 'Зауре'
    person.patronymic = 'Абылкасимовна'
    person.sex = 'Ж'
    person.birthday = '1958-06-24 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-705-870-4826'
    person.father_id = 45
    person.details = 'муж Байзаков Рымбек Нургалиевич 10.02.1957, дети Даурен (1979), Нурлан (1980)'
    person.save()

    person = Person()
    person.id = 84
    person.surname = 'Куватова'
    person.name = 'Бижамал'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1954-06-30 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 85
    person.surname = 'Анапинова (Куватова)'
    person.name = 'Жанат'
    person.patronymic = 'Булатқызы'
    person.sex = 'Ж'
    person.birthday = '1977-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-701-503-5352'    
    person.father_id = 80
    person.mother_id = 84
    person.save()

    person = Person()
    person.id = 86
    person.surname = 'Нет данных'
    person.name = 'Асель'
    person.patronymic = 'Талгатқызы'
    person.sex = 'Ж'
    person.birthday = '2000-01-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.mother_id = 85
    person.save()

    person = Person()
    person.id = 87
    person.surname = 'Нет данных'
    person.name = 'Камила'
    person.patronymic = 'Талгатқызы'
    person.sex = 'Ж'
    person.birthday = '2002-01-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.mother_id = 85
    person.save()

    person = Person()
    person.id = 88
    person.surname = 'Рустимова'
    person.name = 'Бибигуль'
    person.patronymic = 'Булатқызы'
    person.sex = 'Ж'
    person.birthday = '1981-07-30 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-701-556-1007'
    person.details = 'муж Аскар, дети Арсен (2005 г.р.), Амир (2009 г.р.), Айлин (2016 г.р.)'
    person.father_id = 80
    person.mother_id = 84
    person.save()

    person = Person()
    person.id = 89
    person.surname = 'Куватов'
    person.name = 'Қуат'
    person.patronymic = 'Булатұлы'
    person.sex = 'М'
    person.birthday = '1990-01-22 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-707-655-3110'    
    person.father_id = 80
    person.mother_id = 84
    person.save()

    person = Person()
    person.id = 90
    person.surname = 'Куватова'
    person.name = 'Даяна'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1990-01-22 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 91
    person.surname = 'Куватов'
    person.name = 'Асанали'
    person.patronymic = 'Қуатұлы'
    person.sex = 'М'
    person.birthday = '2016-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 89
    person.mother_id = 90
    person.save()

    person = Person()
    person.id = 92
    person.surname = 'Куватова'
    person.name = 'Самира'
    person.patronymic = 'Қуатқызы'
    person.sex = 'Ж'
    person.birthday = '2018-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 89
    person.mother_id = 90
    person.save()
    
    #########

    person = Person()
    person.id = 93
    person.surname = 'Ордабаева'
    person.name = 'Ажар'
    person.patronymic = 'Жаскайратқызы'
    person.sex = 'Ж'
    person.birthday = '1985-11-23 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-707-527-4300'
    person.details = 'муж Бахтыбек, Асанали (2011 г.р.), Айлин (2019 г.р.)'
    person.father_id = 76
    person.save()

    person = Person()
    person.id = 94
    person.surname = 'Абылкасымов'
    person.name = 'Арман'
    person.patronymic = 'Жаскайратулы'
    person.sex = 'М'
    person.birthday = '1985-11-23 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-707-784-5264'
    person.father_id = 76
    person.save()

    person = Person()
    person.id = 95
    person.surname = 'Абылкасымова'
    person.name = 'Кантжан'
    person.patronymic = ''
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1985-11-23 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 96
    person.surname = 'Абылкасымова'
    person.name = 'Дилара'
    person.patronymic = 'Арманқызы'
    person.sex = 'Ж'
    person.birthday = '2008-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.details = 'От первого брака'
    person.father_id = 94
    person.save()

    person = Person()
    person.id = 97
    person.surname = 'Абылкасымов'
    person.name = 'Алимжан'
    person.patronymic = 'Арманұлы'
    person.sex = 'М'
    person.birthday = '2012-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 94
    person.mother_id = 95
    person.save()

    person = Person()
    person.id = 98
    person.surname = 'Абылкасымов'
    person.name = 'Арлан'
    person.patronymic = 'Арманұлы'
    person.sex = 'М'
    person.birthday = '2013-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 94
    person.mother_id = 95
    person.save()

    person = Person()
    person.id = 99
    person.surname = 'Абылкасымова'
    person.name = 'Камила'
    person.patronymic = 'Арманқызы'
    person.sex = 'Ж'
    person.birthday = '2019-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 94
    person.mother_id = 95
    person.save()

    ##########
    
    person = Person()
    person.id = 100
    person.surname = 'Куватов'
    person.name = 'Данияр'
    person.patronymic = 'Муратұлы'
    person.sex = 'М'
    person.birthday = '1987-03-20 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-771-560-8400'    
    person.father_id = 78
    person.mother_id = 79
    person.save()

    person = Person()
    person.id = 101
    person.surname = 'Куватова'
    person.name = 'Бахыт'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1987-03-20 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 102
    person.surname = 'Куватов'
    person.name = 'Аспандияр'
    person.patronymic = 'Даниярұлы'
    person.sex = 'М'
    person.birthday = '2012-03-20 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-771-560-8400'    
    person.father_id = 100
    person.mother_id = 101
    person.save()

    person = Person()
    person.id = 103
    person.surname = 'Куватов'
    person.name = 'Мухамедияр'
    person.patronymic = 'Даниярұлы'
    person.sex = 'М'
    person.birthday = '2016-03-20 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-771-560-8400'    
    person.father_id = 100
    person.mother_id = 101
    person.save()

    ##########

    person = Person()
    person.id = 104
    person.surname = 'Куватова'
    person.name = 'Гульнар'
    person.patronymic = 'Жылқыбайқызы'
    person.sex = 'Ж'
    person.birthday = '1951-11-25 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-702-152-0566'
    person.father_id = 47
    person.save()

    person = Person()
    person.id = 105
    person.surname = 'Куватова'
    person.name = 'Малика'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1992-01-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.mother_id = 104
    person.save()

    person = Person()
    person.id = 106
    person.surname = 'Куватов'
    person.name = 'Нурлан'
    person.patronymic = 'Жылқыбайұлы'
    person.sex = 'М'
    person.birthday = '1950-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 47
    person.save()

    person = Person()
    person.id = 107
    person.surname = 'Куватов'
    person.name = 'Аблай'
    person.patronymic = 'Нурланұлы'
    person.sex = 'М'
    person.birthday = '1970-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 106
    person.save()

    ##########
    
    ##########
    
    person = Person()
    person.id = 108
    person.surname = 'Куватов'
    person.name = 'Амангельды'
    person.patronymic = 'Малгаждарович'
    person.sex = 'М'
    person.birthday = '1947-06-09 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 48
    person.save()

    person = Person()
    person.id = 109
    person.surname = 'Куватова'
    person.name = 'Айкен'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1947-06-09 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 110
    person.surname = 'Куатов'
    person.name = 'Арман'
    person.patronymic = 'Амангельдыұлы'
    person.sex = 'М'
    person.birthday = '1982-03-16 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-777-234-0252'    
    person.father_id = 108
    person.mother_id = 109
    person.save()

    person = Person()
    person.id = 111
    person.surname = 'Куатова'
    person.name = 'Аяулым'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1982-03-16 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 112
    person.surname = 'Куатов'
    person.name = 'Ерлан'
    person.patronymic = 'Амангельдыұлы'
    person.sex = 'М'
    person.birthday = '1988-12-03 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-705-414-5729'    
    person.father_id = 108
    person.mother_id = 109
    person.save()

    person = Person()
    person.id = 113
    person.surname = 'Куатов'
    person.name = 'Жандаулет'
    person.patronymic = 'Ерланұлы'
    person.sex = 'М'
    person.birthday = '2012-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 112
    person.save()

    person = Person()
    person.id = 114
    person.surname = 'Куатов'
    person.name = 'Каусар'
    person.patronymic = 'Ерланұлы'
    person.sex = 'М'
    person.birthday = '2017-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 112
    person.save()

    ##########
    
    person = Person()
    person.id = 115
    person.surname = 'Куватов'
    person.name = 'Исатай'
    person.patronymic = 'Малгаждарович'
    person.sex = 'М'
    person.birthday = '1950-09-23 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-705-481-6000'
    person.father_id = 48
    person.save()

    ##########
    
    person = Person()
    person.id = 116
    person.surname = 'Куватов'
    person.name = 'Естай'
    person.patronymic = 'Малгаждарович'
    person.sex = 'М'
    person.birthday = '1957-09-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-705-140-4642'
    person.father_id = 48
    person.save()

    person = Person()
    person.id = 117
    person.surname = 'Куватова'
    person.name = 'Лариса'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1957-09-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 118
    person.surname = 'Куватова'
    person.name = 'Ольга'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1957-09-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    ##########
    
    person = Person()
    person.id = 119
    person.surname = 'Куватов'
    person.name = 'Бауыржан'
    person.patronymic = 'Малгаждарович'
    person.sex = 'М'
    person.birthday = '1961-07-05 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-701-111-0222'
    person.father_id = 48
    person.save()
    
    person = Person()
    person.id = 120
    person.surname = 'Куватова'
    person.name = 'Сандугаш'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1961-07-05 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    ###########
    
    person = Person()
    person.id = 121
    person.surname = 'Куватов'
    person.name = 'Алтынбек'
    person.patronymic = 'Малгаждарович'
    person.sex = 'М'
    person.birthday = '1964-07-14 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-777-587-7751'
    person.father_id = 48
    person.save()

    person = Person()
    person.id = 122
    person.surname = 'Куватова'
    person.name = 'Бахыт'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1964-07-14 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    ##########

    person = Person()
    person.id = 123
    person.surname = 'Куватова'
    person.name = 'Айжан'
    person.patronymic = 'Естайқызы'
    person.sex = 'Ж'
    person.birthday = '1975-01-02 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-705-508-6623'    
    person.father_id = 116
    person.mother_id = 118
    person.save()

    person = Person()
    person.id = 124
    person.surname = 'Куватова'
    person.name = 'Мадина'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1994-01-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.mother_id = 123
    person.save()

    person = Person()
    person.id = 125
    person.surname = 'Куватов'
    person.name = 'Тимур'
    person.patronymic = 'Естайұлы'
    person.sex = 'М'
    person.birthday = '1978-05-05 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-707-222-4361'    
    person.father_id = 116
    person.mother_id = 118
    person.save()

    person = Person()
    person.id = 126
    person.surname = 'Куватова'
    person.name = 'Ольга'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1978-05-05 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 127
    person.surname = 'Куватова'
    person.name = 'Диана'
    person.patronymic = 'Тимурқызы'
    person.sex = 'Ж'
    person.birthday = '2001-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 125
    person.mother_id = 126
    person.save()

    person = Person()
    person.id = 128
    person.surname = 'Куватова'
    person.name = 'Дарина'
    person.patronymic = 'Тимурқызы'
    person.sex = 'Ж'
    person.birthday = '2010-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 125
    person.mother_id = 126
    person.save()

    person = Person()
    person.id = 129
    person.surname = 'Куватов'
    person.name = 'Руслан'
    person.patronymic = 'Естайұлы'
    person.sex = 'М'
    person.birthday = '1986-08-26 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-701-777-4367'    
    person.father_id = 116
    person.mother_id = 118
    person.save()

    person = Person()
    person.id = 130
    person.surname = 'Куватова'
    person.name = 'Айша'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1986-08-26 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 131
    person.surname = 'Куватова'
    person.name = 'Камила'
    person.patronymic = 'Русланқызы'
    person.sex = 'Ж'
    person.birthday = '2008-08-26 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 129
    person.mother_id = 130
    person.save()

    person = Person()
    person.id = 132
    person.surname = 'Куватова'
    person.name = 'Томирис'
    person.patronymic = 'Русланқызы'
    person.sex = 'Ж'
    person.birthday = '2008-08-26 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 129
    person.mother_id = 130
    person.save()

    person = Person()
    person.id = 133
    person.surname = 'Куватова'
    person.name = 'Ясмин'
    person.patronymic = 'Русланқызы'
    person.sex = 'Ж'
    person.birthday = '2015-08-26 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 129
    person.mother_id = 130
    person.save()

    person = Person()
    person.id = 134
    person.surname = 'Куватов'
    person.name = 'Мөнгіліқ'
    person.patronymic = 'Естайұлы'
    person.sex = 'М'
    person.birthday = '1995-07-26 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-701-082-4268'    
    person.father_id = 116
    person.mother_id = 118
    person.save()

    person = Person()
    person.id = 135
    person.surname = 'Куватова'
    person.name = 'Дана'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1995-07-26 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 136
    person.surname = 'Малгаждарова'
    person.name = 'Анель'
    person.patronymic = 'Естайқызы'
    person.sex = 'Ж'
    person.birthday = '1997-02-13 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-707-721-6934'    
    person.father_id = 116
    person.mother_id = 118
    person.save()

    person = Person()
    person.id = 137
    person.surname = 'Куватов'
    person.name = 'Ельдар'
    person.patronymic = 'Бауыржанұлы'
    person.sex = 'М'
    person.birthday = '1990-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-701-779-8888'
    person.father_id = 119
    person.mother_id = 120    
    person.save()

    person = Person()
    person.id = 138
    person.surname = 'Куватов'
    person.name = 'Рустам'
    person.patronymic = 'Алтынбекұлы'
    person.sex = 'М'
    person.birthday = '1989-07-11 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-702-882-8889'
    person.father_id = 121
    person.mother_id = 122    
    person.save()

    person = Person()
    person.id = 139
    person.surname = 'Куватов'
    person.name = 'Данияр'
    person.patronymic = 'Алтынбекұлы'
    person.sex = 'М'
    person.birthday = '1988-03-02 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.phone = '+7-705-507-4705'    
    person.father_id = 121
    person.mother_id = 122    
    person.save()

    person = Person()
    person.id = 140
    person.surname = 'Куватова'
    person.name = 'Жибек'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1988-03-02 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 141
    person.surname = 'Куватов'
    person.name = 'Алиамир'
    person.patronymic = 'Даниярұлы'
    person.sex = 'М'
    person.birthday = '2017-03-02 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 139
    person.mother_id = 140
    person.save()

    person = Person()
    person.id = 142
    person.surname = 'Куватов'
    person.name = 'Диас'
    person.patronymic = 'Бауыржанұлы'
    person.sex = 'М'
    person.birthday = '2003-01-01 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 70
    person.mother_id = 71    
    person.save()

    person = Person()
    person.id = 143
    person.surname = 'Махметов'
    person.name = 'Жумаш'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1946-01-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 144
    person.surname = 'Махметов'
    person.name = 'Жанат'
    person.patronymic = 'Жумашұлы'
    person.sex = 'М'
    person.birthday = '1968-01-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.father_id = 143
    person.mother_id = 77
    person.details = 'супруга Маржан, сын - Аскар'
    person.save()
    
    person = Person()
    person.id = 145
    person.surname = 'Махметова'
    person.name = 'Гульдана'
    person.patronymic = 'Жумашұлы'
    person.sex = 'Ж'
    person.birthday = '1977-01-27 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.father_id = 143
    person.mother_id = 77
    person.details = 'дети - Багустар (1999), Бахтияр (2003)'
    person.save()
    person = Person()

    person = Person()
    person.id = 146
    person.surname = 'Махметов'
    person.name = 'Дастан'
    person.patronymic = 'Жумашұлы'
    person.sex = 'М'
    person.birthday = '1981-02-09 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.father_id = 143
    person.mother_id = 77
    person.details = 'супруга Меруерт'
    person.save()

    person = Person()
    person.id = 147
    person.surname = 'Мусралин'
    person.name = 'Есимжан'
    person.patronymic = ''
    person.sex = 'М'
    person.birthday = '1911-01-01 12:00:00'
    person.tribe = 'Найман'
    person.clan = 'Актiлес'
    person.save()

    person = Person()
    person.id = 148
    person.surname = 'Мусралинова'
    person.name = 'Катима'
    person.patronymic = ''
    person.sex = 'Ж'
    person.birthday = '1911-01-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 149
    person.surname = 'Анапинов'
    person.name = 'Аскер'
    person.patronymic = 'Бейсембаевич'
    person.sex = 'М'
    person.birthday = '1978-02-23 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.save()

    person = Person()
    person.id = 150
    person.surname = 'Анапинова'
    person.name = 'Еркежан'
    person.patronymic = 'Аскерқызы'
    person.sex = 'Ж'
    person.birthday = '2021-01-01 12:00:00'
    person.tribe = ''
    person.clan = ''
    person.father_id = 149
    person.mother_id = 85
    person.save()

    person = Person()
    person.id = 151
    person.surname = 'Куватов'
    person.name = 'Омар'
    person.patronymic = 'Мөнгіліқұлы'
    person.sex = 'М'
    person.birthday = '2022-05-18 12:00:00'
    person.tribe = 'Арғын'
    person.clan = 'Қанжығалы'
    person.father_id = 134
    person.mother_id = 135
    person.save()


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(new_person),
        migrations.RunSQL("""CREATE VIEW person_list AS
            SELECT id, iif( surname = "Нет данных", "", surname || ' ')  || name  || iif(patronymic NOT Null, ' '  || patronymic, '') AS fio,
            sex, birthday, iif(strftime('%Y',birthday)>"1900", strftime('%d.%m.%Y',birthday),"") AS birthday20, tribe, clan, phone, address, email, photo, details, father_id,
            (SELECT iif( surname = "Нет данных", "", surname || ' ')  || name || iif(patronymic NOT Null, ' '  || patronymic, '')  FROM Person f WHERE f.id=p.father_id) AS father,
            mother_id, (SELECT iif( surname = "Нет данных", "", surname || ' ')  || name || iif(patronymic NOT Null, ' '  || patronymic, '')  FROM Person m WHERE m.id=p.mother_id) AS mother,
            (SELECT GROUP_CONCAT(name ||  iif(strftime('%Y',birthday)>"1900", ' (' || strftime('%Y',birthday) || ')',"") ,'; ')
            FROM Person c WHERE c.father_id=p.id ORDER BY birthday) AS children FROM Person p;"""),
#        migrations.RunSQL("""CREATE VIEW person_list AS 
#        SELECT id, 
#	CASE WHEN surname = 'Нет данных' THEN name 
#		ELSE surname || ' '  || name  
#		|| 
#	CASE WHEN patronymic IS Null THEN ''  
#		ELSE ' ' || patronymic
#	END
#	END
#	AS fio, sex, birthday, 
#	CASE WHEN EXTRACT(YEAR FROM birthday) >1900 THEN to_char( birthday, 'DD-MM-YYYY')
#	ELSE ''
#	END
#	AS birthday20, tribe, clan, phone, address, email, photo, details, father_id, 
#(SELECT 
# 	CASE WHEN surname = 'Нет данных' THEN name
# 	ELSE surname || ' ' || name || 
# 	CASE WHEN patronymic IS Null THEN ''  
# 	ELSE ' ' || patronymic
# 	END
# 	END 
# FROM Person f WHERE f.id=p.father_id) AS father, mother_id, 
# (SELECT 
# 	CASE WHEN surname = 'Нет данных' THEN name
# 	ELSE surname || ' ' || name || 
# 	CASE WHEN patronymic IS Null THEN ''  
# 	ELSE ' ' || patronymic
# 	END
# 	END 
# FROM Person f WHERE f.id=p.mother_id) AS mother, 
#  (SELECT array_agg(name ||  
#	CASE WHEN EXTRACT(YEAR FROM birthday) >1900 THEN ' (' || to_char( birthday, 'YYYY') || ')'
#	ELSE ''
#	END
#    ) FROM Person c WHERE c.father_id=p.id) AS children FROM Person p;"""),    
    ]
