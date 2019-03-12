
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    icons = models.ImageField(upload_to='images/')
    votes = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.TextField()

    def __str__(self):
        return self.title

    def summery(self):
        return  self.body[0:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime( ' %b %e %y ' )