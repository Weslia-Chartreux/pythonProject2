from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Community(models.Model):
    name = models.CharField(max_length=100)
    header = models.CharField(max_length=400)
    description = models.TextField()
    rules = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(Community, on_delete=models.CASCADE, blank=True, null=True, related_name='posts')
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-date"]
