from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=4000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

