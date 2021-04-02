from datetime import datetime

from delorean import utcnow
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


def _utcnow() -> datetime:
    return utcnow().datetime


class Post(models.Model):
    author = models.ForeignKey(
        User,
        blank=True,
        db_index=True,
        null=True,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        db_index=True,
        default=_utcnow,
    )
    title = models.CharField(
        blank=True,
        max_length=200,
        null=True,
    )
    content = models.TextField(
        blank=True,
        null=True,
    )
    image = models.URLField(
        blank=True,
        null=True,
    )
    nr_views = models.IntegerField(
        default=0,
    )
    nr_likes = models.IntegerField(
        default=0,
    )

    class Meta:
        ordering = ["-created_at", "title", "author_id", "id"]

    def __str__(self) -> str:
        return f"{self.title} ({self.pk})"

    def get_absolute_url(self) -> str:
        return f"/b/p/{self.pk}/"
