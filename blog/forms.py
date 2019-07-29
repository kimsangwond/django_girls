from django import forms
from .models import Post

class PostForm(forms.ModelForm): # 이 폼이 ModelForm이라는 것을 알려줌
    class Meta: # 폼을 만들기 위해서 어떤 model이 쓰여야 하는지 알려주기 위함
        model = Post # Post가 모델로 쓰인다고 명시
        fields = ('title', 'text',) # form에 title과 text가 보이게 함