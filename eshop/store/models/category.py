from django.db import models
class Cetegory(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name



    @staticmethod
    def get_all_catagary():
        item=Cetegory.objects.all()
        return item    
