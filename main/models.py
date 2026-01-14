from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100,unique=True
    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('prog', 'В процессе'),
        ('cancel', 'Отменена'),
        ('complete', 'Завершена'),

    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    goal_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='prog')
    important = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['add_date', 'goal_date', 'status']


