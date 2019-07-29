from django.shortcuts import render  # render import
from .models import Post  # models 함수의 Post 객체 불러오기
from django.utils import timezone #timzone import


def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# post_list 함수: request를 넘겨받아 rener 메소드 호출
# rednder 함수: blog/post_list.html 템플릿을 호출
# posts: 쿼리셋의 이름
