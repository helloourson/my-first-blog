from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
# Blogpost-Model
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ForeignKey definiert Verknüpfung/ Beziehung zu einen anderen Model
    title = models.CharField(max_length=200)  # Texfeld mit limitierten Anzahl von Zeichen
    text = models.TextField()  # Texfeld ohne Grössenbeschränkung
    created_date = models.DateTimeField(default=timezone.now)  # Feld für einen Zeitpunkt Datum und Uhrzeit
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
