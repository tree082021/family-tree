from django.shortcuts import render, redirect

# Класс HttpResponse из пакета django.http, который позволяет отправить текстовое содержимое.
from django.http import HttpResponse, HttpResponseNotFound
# Конструктор принимает один обязательный аргумент – путь для перенаправления. Это может быть полный URL (например, 'https://www.yahoo.com/search/') или абсолютный путь без домена (например, '/search/').
from django.http import HttpResponseRedirect

from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Подключение моделей
from .models import Person, PersonList
# Подключение форм
from .forms import PersonForm, SignUpForm

from anytree.importer import DictImporter
from anytree import RenderTree
from anytree import Node
from anytree.exporter import DotExporter

import xlwt
from io import BytesIO

from django.db import models

import sys

from django.utils import timezone

from django.utils.translation import gettext_lazy as _

from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy

from django.contrib.auth import login as auth_login


# Групповые ограничения
def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, login_url='403')

# Стартовая страница с выводом Шежіре
def index(request):
    man = Person.objects.all().filter(sex='М', tribe = 'Арғын', clan='Қанжығалы').order_by('birthday')
    root = Node("Орта жүз")
    # Самый ранний отец, не внесенный в базу данных
    a0 = Node("Арғын", root)
    idx='id'
    for m in man:
        # Поле, которое выводится в качетсве узладереве
        y=m.name
        if m.father_id is None:
            z=idx + str(0)
        else:
            z=globals()['id%s' % m.father_id]
        # Самый ранний отец, внесенный в базу данных, его отец a0, для остальных отцы берутся из базы данных
        if m.id==1:
            z=a0
            globals()['id%s' % m.id] = Node(y, z)
        else:
            if m.father_id is not None:
                globals()['id%s' % m.id] = Node(y, z)
    # Вывод в консоль
    #print(RenderTree(root).by_attr())

    ## Вывод в файл, перенаправление вывода
    #orig_stdout = sys.stdout
    #somefile = open("c:/temp/tree.txt", "w", encoding="utf-8")    
    #sys.stdout = somefile
    #print(RenderTree(root).by_attr())
    #somefile.close()
    ## Возврат вывода в стандартное состояние
    #sys.stdout = sys.__stdout__

    tree = list()
    for pre, __, node in RenderTree(root):
        tree.append("%s%s" % (pre, node.name))
        #print("%s%s" % (pre, node.name))    
    return render(request, "index.html", {"man": man, "tree":tree})    

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def person_index(request):
    #person = Person.objects.all().order_by('surname', 'name', 'patronymic')
    #return render(request, "person/index.html", {"person": person})
    person_list = PersonList.objects.all().order_by('birthday', 'fio')
    return render(request, "person/index.html", {"person_list": person_list})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def person_create(request):
    try:
        if request.method == "POST":
            person = Person()
            person.surname = request.POST.get("surname")
            person.name = request.POST.get("name")
            person.patronymic = request.POST.get("patronymic")
            person.sex = request.POST.get("sex")
            person.birthday = request.POST.get("birthday")
            person.tribe = request.POST.get("tribe")
            person.clan = request.POST.get("clan")
            person.phone = request.POST.get("phone")
            person.address = request.POST.get("address")
            person.email = request.POST.get("email")
            if 'photo' in request.FILES:                
                person.photo = request.FILES['photo']        
            person.details = request.POST.get("details")
            if request.POST.get('father') != "":
                person.father = Person.objects.filter(id=request.POST.get("father")).first()
            if request.POST.get('mother') !="":
                person.mother = Person.objects.filter(id=request.POST.get("mother")).first()
            personform = PersonForm(request.POST)
            if personform.is_valid():
                person.save()
                return HttpResponseRedirect(reverse('person_index'))
            else:
                return render(request, "person/create.html", {"form": personform})
        else:            
            personform = PersonForm(initial={'birthday': timezone.now().strftime('%Y-%m-%d'), })        
            return render(request, "person/create.html", {"form": personform})
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
# И вначале по этому идентификатору мы пытаемся найти объект с помощью метода Person.objects.get(id=id).
# Поскольку в случае отсутствия объекта мы можем столкнуться с исключением Person.DoesNotExist,
# то соответственно нам надо обработать подобное исключение, если вдруг будет передан несуществующий идентификатор.
# И если объект не будет найден, то пользователю возващается ошибка 404 через вызов return HttpResponseNotFound().
# Если объект найден, то обработка делится на две ветви.
# Если запрос POST, то есть если пользователь отправил новые изменненые данные для объекта, то сохраняем эти данные в бд и выполняем переадресацию на корень веб-сайта.
# Если запрос GET, то отображаем пользователю страницу edit.html с формой для редактирования объекта.
@login_required
@group_required("Managers")
def person_edit(request, id):
    try:
        person = Person.objects.get(id=id) 
        if request.method == "POST":
            person.surname = request.POST.get("surname")
            person.name = request.POST.get("name")
            person.patronymic = request.POST.get("patronymic")
            person.sex = request.POST.get("sex")
            person.birthday = request.POST.get("birthday")
            person.tribe = request.POST.get("tribe")
            person.clan = request.POST.get("clan")
            person.phone = request.POST.get("phone")
            person.address = request.POST.get("address")
            person.email = request.POST.get("email")
            if "photo" in request.FILES:                
                person.photo = request.FILES["photo"]
            person.details = request.POST.get("details")
            if request.POST.get('father') != "":
                person.father = Person.objects.filter(id=request.POST.get("father")).first()
            if request.POST.get('mother') !="":
                person.mother = Person.objects.filter(id=request.POST.get("mother")).first()
            personform = PersonForm(request.POST)
            if personform.is_valid():
                person.save()
                return HttpResponseRedirect(reverse('person_index'))
            else:
                return render(request, "person/edit.html", {"form": personform})
        else:
            # Загрузка начальных данных
            personform = PersonForm(initial={'surname': person.surname, 'name': person.name, 'patronymic': person.patronymic, 'sex': person.sex, 'birthday': person.birthday.strftime('%Y-%m-%d'), 'tribe': person.tribe,'clan': person.clan,'phone': person.phone,'address': person.address, 'email': person.email, 'photo': person.photo, 'details': person.details, 'father': person.father, 'mother': person.mother })
            return render(request, "person/edit.html", {"form": personform})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def person_delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect(reverse('person_index'))
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Просмотр страницы read.html для просмотра объекта.
@login_required
def person_read(request, id):
    try:
        person_list = PersonList.objects.get(id=id) 
        return render(request, "person/read.html", {"person_list": person_list})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Список персон (с детьми)
@login_required
@group_required("Managers","Readers")
def catalog(request):
    person_list = PersonList.objects.all().order_by('birthday', 'fio')
    return render(request, "catalog.html", {"person_list": person_list})    
     
def contact(request):
    return render(request, "contact.html")

# Регистрационная форма 
def signup(request):
    try:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('index')
                #return render(request, 'registration/register_done.html', {'new_user': user})
        else:
            form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email',)
    template_name = 'registration/my_account.html'
    success_url = reverse_lazy('index')
    #success_url = reverse_lazy('my_account')
    def get_object(self):
        return self.request.user

# Экспорт в Рисунок
@login_required
@group_required("Managers","Readers")
def export_person_chart(request):
    try:
        man = PersonList.objects.all().filter(sex='М', tribe = 'Арғын', clan='Қанжығалы').order_by('birthday')
        root = Node("Орта жүз")
        # Самый ранний отец, не внесенный в базу данных
        a0 = Node("Арғын", root)
        idx='id'
        for m in man:
            # Поле, которое выводится в качетсве узладереве
            y=m.fio
            if m.father_id is None:
                z=idx + str(0)
            else:
                z=globals()['id%s' % m.father_id]
            # Самый ранний отец, внесенный в базу данных, его отец a0, для остальных отцы берутся из базы данных
            if m.id==1:
                z=a0
                globals()['id%s' % m.id] = Node(y, z)
            else:
                if m.father_id is not None:
                    globals()['id%s' % m.id] = Node(y, z)
        # Вывод в консоль
        #print(RenderTree(root).by_attr())
        # Вывод в рисунок
        from tempfile import NamedTemporaryFile
        import os
        from django.core.files.base import File
        temp_file = NamedTemporaryFile(delete=True)
        #print(temp_file.name)
        temp_file.name = temp_file.name + ".png"
        DotExporter(root,
            nodeattrfunc=lambda node: "fixedsize=false, width=1, height=1",
            edgeattrfunc=lambda parent, child: "style=bold"
            ).to_picture(temp_file.name)

        from django.http import FileResponse
        response = FileResponse(open(temp_file.name, 'rb'))
        response['Content-Disposition'] = 'attachment; filename=chart.png' 
        return response

        #path_to_file = os.path.realpath(temp_file.name + ".png")
        #f = open(path_to_file, 'r')
        #myfile = File(f)
        #response = HttpResponse(myfile, content_type='image/png')
        #response['Content-Disposition'] = 'attachment; filename=chart.png'
        #return response

        #return render(request, "chart.html", {"src": "file:///" + temp_file.name.replace("\\","/")})
        
    except Exception:        
        return HttpResponse("<p>Для создания рисунка дерева - на компьютере необходимо установить Graphviz (<a href='http://www.graphviz.org/'>http://www.graphviz.org/</a>)</p><p><a style='align:center' href='javascript:history.back();'>Назад</a></p>")
    
# Экспорт в Excel
@login_required
@group_required("Managers","Readers")
def export_person_excel(request): 
    try:
        # Create a HttpResponse object and set its content_type header value to Microsoft excel.
        response = HttpResponse(content_type='application/vnd.ms-excel') 
        # Set HTTP response Content-Disposition header value. Tell web server client the attached file name is students.xls.
        response['Content-Disposition'] = 'attachment;filename=tree.xls' 
        # Create a new Workbook file.
        work_book = xlwt.Workbook(encoding = 'utf-8') 
        # Create a new worksheet in the above workbook.
        work_sheet = work_book.add_sheet(u'Person Info')
        # Maintain some worksheet styles，style_head_row, style_data_row, style_green, style_red
        # This style will be applied to worksheet head row.
        style_head_row = xlwt.easyxf("""    
            align:
              wrap off,
              vert center,
              horiz center;
            borders:
              left THIN,
              right THIN,
              top THIN,
              bottom THIN;
            font:
              name Arial,
              colour_index white,
              bold on,
              height 0xA0;
            pattern:
              pattern solid,
              fore-colour 0x19;
            """
        )
        # Define worksheet data row style. 
        style_data_row = xlwt.easyxf("""
            align:
              wrap on,
              vert center,
              horiz left;
            font:
              name Arial,
              bold off,
              height 0XA0;
            borders:
              left THIN,
              right THIN,
              top THIN,
              bottom THIN;
            """
        )
        # Set data row date string format.
        style_data_row.num_format_str = 'dd/mm/yyyy'
        # Define a green color style.
        style_green = xlwt.easyxf(" pattern: fore-colour 0x11, pattern solid;")
        # Define a red color style.
        style_red = xlwt.easyxf(" pattern: fore-colour 0x0A, pattern solid;")
        # Generate worksheet head row data.
        work_sheet.write(0,0, _('father'), style_head_row) 
        work_sheet.write(0,1, _('mother'), style_head_row) 
        work_sheet.write(0,2, _('fio'), style_head_row)
        if request.user.groups.filter(name = "Managers").exists():
            work_sheet.write(0,3, _('sex'), style_head_row) 
            work_sheet.write(0,4, _('birthday'), style_head_row) 
            work_sheet.write(0,5, _('tribe'), style_head_row) 
            work_sheet.write(0,6, _('clan'), style_head_row) 
            work_sheet.write(0,7, _('phone'), style_head_row) 
            work_sheet.write(0,8, _('address'), style_head_row) 
            work_sheet.write(0,9, _('email'), style_head_row) 
            work_sheet.write(0,10, _('details'), style_head_row)
            work_sheet.write(0,11, _('children'), style_head_row)
        else:
            work_sheet.write(0,3, _('children'), style_head_row) 
        # Generate worksheet data row data.
        row = 1 
        for p in PersonList.objects.all():
            work_sheet.write(row,0, p.father, style_data_row)
            work_sheet.write(row,1, p.mother, style_data_row)
            work_sheet.write(row,2, p.fio, style_data_row)
            if request.user.groups.filter(name = "Managers").exists():            
                work_sheet.write(row,3, p.sex, style_data_row)
                #work_sheet.write(row,4, p.birthday.strftime('%d.%m.%Y'), style_data_row)
                work_sheet.write(row,4, p.birthday20, style_data_row)
                work_sheet.write(row,5, p.tribe, style_data_row)
                work_sheet.write(row,6, p.clan, style_data_row)
                work_sheet.write(row,7, p.phone, style_data_row)
                work_sheet.write(row,8, p.address, style_data_row)
                work_sheet.write(row,9, p.email, style_data_row)
                work_sheet.write(row,10, p.details, style_data_row)
                work_sheet.write(row,11, str(p.children).replace(',',';'), style_data_row)            
            else:
                work_sheet.write(row,3, str(p.children).replace(',',';'), style_data_row)
            row=row + 1 
        # Create a StringIO object.
        output = BytesIO()
        # Save the workbook data to the above StringIO object.
        work_book.save(output)
        # Reposition to the beginning of the StringIO object.
        output.seek(0)
        # Write the StringIO object's value to HTTP response to send the excel file to the web server client.
        response.write(output.getvalue()) 
        return response
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)
