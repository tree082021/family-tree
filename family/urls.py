"""family URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Модуль содержит код Python, который отображает URL-шаблоны (регулярные выражения)
# и связанные функции Python (ваши представления).

from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings 
from django.conf.urls.static import static 
from django.conf.urls import include

from tree import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('catalog/', views.catalog, name='catalog'),
    path('contact/', views.contact, name='contact'),        
        
    path('person/index/', views.person_index, name='person_index'),
    path('person/create/', views.person_create, name='person_create'),
    path('person/edit/<int:id>/', views.person_edit, name='person_edit'),
    path('person/delete/<int:id>/', views.person_delete, name='person_delete'),
    path('person/read/<int:id>/', views.person_read, name='person_read'),

    path('export/excel/', views.export_person_excel, name='export_person_excel'),
    path('export/chart/', views.export_person_chart, name='export_person_chart'),

    path('signup/', views.signup, name='signup'),    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('settings/account/', views.UserUpdateView.as_view(), name='my_account'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    """
    url(r'^parents/index/', views.parents_index, name='parents_index'),
    re_path(r'^parents/create/', views.parents_create, name='parents_create'),
    re_path(r'^parents/edit/(?P<id>\d+)/', views.parents_edit, name='parents_edit'),
    re_path(r'^parents/delete/(?P<id>\d+)/', views.parents_delete, name='parents_delete'),
    """
