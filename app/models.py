from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_deadline = models.DateTimeField(blank=True, null=True)
    task_is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return f"{self.content} ({self.task_is_done})"

    class Meta:
        ordering = ["task_is_done", "-date_created"]
