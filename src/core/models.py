from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(default="No description", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs) -> None:
        if not self.body: self.body = "No description"
        super(Todo, self).save(*args, **kwargs)

    def __str__(self) -> None:
        return self.title

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
