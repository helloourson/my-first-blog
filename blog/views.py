from django.shortcuts import render
#Datenbank Model Post importieren
# .models da models.py im geleichen Ordner liegt
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.

def post_list(request):
    #QuerySet
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

#Detail Blog ansehen
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
