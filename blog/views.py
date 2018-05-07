from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    #현재 시간 기준 과거에 작성했던 게시글 모두를 가져오고 게시일 기준으로 정렬해서 가져오는 구문
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
