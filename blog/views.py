from django.shortcuts import render  # render import
from .models import Post  # models 함수의 Post 객체 불러오기
from django.utils import timezone #timzone import
from django.shortcuts import render, get_object_or_404 # page not found page 제
from .forms import PostForm # Postform import
from django.shortcuts import redirect



def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# post_list 함수: request를 넘겨받아 rener 메소드 호출
# rednder 함수: blog/post_list.html 템플릿을 호출
# posts: 쿼리셋의 이름


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) #url로 부터 받은 pk 값에 해당하는 post가 없을 경우 page not found 제
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)  # request.POST에 저장된 데이터를 PostForm으로 폼에게 넘겨줌
        if form.is_valid(): # 폼에 들어있는 값들이 올바른지를 확인
            post = form.save(commit=False) # commit=False란 넘겨진 데이터를 바로 Post 모델에 저장하지는 말라는 뜻
            post.author = request.user
            post.published_date = timezone.now()
            post.save() # post.save()는 변경사항(작성자 정보를 포함)을 유지
            return redirect('post_detail', pk=post.pk) # post_detail 파일이 pk값을 필요로 하기 때문에 이번에 생성한 post의 pk를 리턴
    else:  # 맨 처음 화면에 왔을 때 get 방식이기 때문에 else 조건문으로 감
        form = PostForm()  # POST로 넘겨진 폼 필드의 값들은 이제 request.POST에 저장
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})