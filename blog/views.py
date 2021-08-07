from django.shortcuts import render
#Datenbank Model Post importieren
# .models da models.py im geleichen Ordner liegt
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
    #QuerySet
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

#Detail Blog ansehen
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

#Formular für neuen Blog
def post_new(request):
    if request.method == "POST": #Wenn
        form = PostForm(request.POST) #PostForm nimmt die ausgefüllten Daten im Forumlar auf
        if form.is_valid() :
            post = form.save(commit=False) #Model hier noch nicht speichern
            post.author = request.user
            post.published_date = timezone.now()
            post.save() #Formular abspeichern
            # Um zum neu erzeugten Detail-Blog zu gehen, wird post_detail view aufgerufen
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

#Formular für Bearbeitung von bestehenden Blogs
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False) #Model hier noch nicht speichern
            post.author = request.user
            post.published_date = timezone.now()
            post.save() #Formular abspeichern
            # Um zum neu erzeugten Detail-Blog zu gehen, wird post_detail view aufgerufen
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})
