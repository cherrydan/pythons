from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name='post_list'),
    #шаблон заголовка url слово post, косая черта, primary key и еще косая черта
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #роутинг для добавления нового поста
    path('post/new/', views.post_new, name='post_new'),
]