from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
]

""" Wie du siehst, fügen wir nun eine view mit dem Namen post_list zur Root-URL hinzu.
Leere Zeichenfolgen passen auf dieses Muster und der Django-URL-Resolver ignoriert den
Domain-Namen (z.B. http://127.0.0.1:8000/), der im vollständigen Pfad voransteht.
Dieses Muster sagt Django also, dass views.post_list das gewünschte Ziel ist, wenn jemand
deine Website über 'http://127.0.0.1:8000/' aufruft. """

""" Der letzte Teil name='post_list' ist der Name der URL, der genutzt wird, um die View zu
identifizieren. Er kann identisch mit dem Namen der View sein, aber es kann auch ein komplett
anderer sein. Wir werden später die Namen der URLs im Projekt benutzen. Daher ist es wichtig, jede
URL in der App zu benennen. Wir sollten außerdem versuchen, eindeutige und einfach zu merkende URL-Namen zu wählen."""
