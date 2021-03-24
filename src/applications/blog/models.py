from django.db import models


class Post(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    content = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    nr_views = models.IntegerField(default=0)
    nr_likes = models.IntegerField(default=0)

    class Meta:
        ordering = ["title", "-id"]

    def __str__(self) -> str:
        return f"{self.title} ({self.pk})"

    def get_absolute_url(self) -> str:
        return f"/b/p/{self.pk}/"
