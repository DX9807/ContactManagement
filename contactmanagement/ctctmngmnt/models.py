from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.name
        