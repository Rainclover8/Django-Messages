from django.db import models



# Create your models here.
class createMessage(models.Model):
    username = models.CharField(max_length=40, verbose_name="isim", null=False)
    description = models.TextField(verbose_name="Söz", null=False)
    
    def __str__(self):
        return self.username