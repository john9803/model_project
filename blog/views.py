from django.shortcuts import render
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects # 전달받은 객체 : 쿼리셋, 쿼리셋의 여러가지 기능들을 표현하는기능 : 메소드
    return render(request, 'home.html', {'blogs' : blogs})

# 쿼리셋과 메소드 형식
# 모델.쿼리셋(objects).메소드