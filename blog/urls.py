from django.urls import path
from . import views #blog views 가져오기

urlpatterns = [
    path('', views.post_list, name='post_list'), #/blog/ url로 접속하면 view의 post_list 보여줌
]