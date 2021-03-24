from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        null=True,
        blank=True,
    )
    title = models.CharField(
        null=True,
        blank=True,
        max_length=200,
    )
    content = models.TextField(
        null=True,
        blank=True,
    )
    image = models.URLField(
        null=True,
        blank=True,
    )
    nr_views = models.IntegerField(
        default=0,
    )
    nr_likes = models.IntegerField(
        default=0,
    )

    class Meta:
        ordering = ["title", "-id"]

    def __str__(self) -> str:
        return f"{self.title} ({self.pk})"

    def get_absolute_url(self) -> str:
        return f"/b/p/{self.pk}/"
