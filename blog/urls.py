from django.urls import path
from . import views #blog views 가져오기

urlpatterns = [
    path('', views.post_list, name='post_list'), #/blog/ url로 접속하면 view의 post_list 보여줌
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # <int: pk>: 장고는 정수 값을 기대하고 이를 pk라는 변수로 뷰로 전송
]