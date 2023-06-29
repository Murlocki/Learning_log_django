from django.urls import path, re_path
from . import views

# Определяет схемы url для learning_logs

# Список страниц которые могут запрашивать приложения из learning_logs
urlpatterns = [
   # Определяем url между началом и конца которых ничего нет
   # Создаем индек для ссылки на эту страницу

   # Домашняя страница
   re_path(r'^$', views.index, name='index'),
   path('topics/', views.topics, name='topics'),
   re_path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
   re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
   re_path(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
   re_path(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry')
]