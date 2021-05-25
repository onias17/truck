from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(
        'Phone Number',
        max_length=13
    )
    email = models.EmailField(max_length=100)
    message = models.TextField(
        'Let us know what you need!',
        max_length=500
    )
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.email