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
    if request.method == "POST": #Wenn request-Methode "POST" ist diesen Code ausführen
        form = PostForm(request.POST) #PostForm nimmt die ausgefüllten Daten im Forumlar auf
        if form.is_valid() :
            post = form.save(commit=False) #Model hier noch nicht speichern
            post.author = request.user #Als Author wird angemeldeter user verwendet
            post.published_date = timezone.now() #Das akutelle Datum, Uhrzeit wird verwendet
            post.save() #Formular abspeichern
            # Um zum neu erzeugten Detail-Blog zu gehen, wird post_detail view aufgerufen
            return redirect('post_detail', pk=post.pk)

    else: #Wenn Plus-Ikon angelickt wird soll dieser Code ausgefürht werden, request-Methode ist in diesem
        # Fall nicht POST und ein leeres Formular soll angezeigt werden
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

#Formular für Bearbeitung von bestehenden Blogs
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False) #Model hier noch nicht speichern
            post.author = request.user #Authro automatisch hinzufügen, da user eingeloggt ist ist das möglich
            post.published_date = timezone.now() #Aktuelles Datum und Uhrzeit hinzufügen
            post.save() #Formular wird jeztz gespeichert
            # Um zum neu erzeugten Detail-Blog zu gehen, wird post_detail view aufgerufen
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})
