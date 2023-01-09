from audioop import reverse
from django.db import models
from django.utils import timezone

# Create your models here.
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class Type(models.Model):
    title = models.CharField(max_length=150, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("type", args=[self.id])


class Note(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "note", args=[str(self.todo_list.id), str(self.id)]
        )

    class Meta:
        ordering = ["due_date"]