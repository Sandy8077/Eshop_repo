from django.db import models
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=15)


    def register(self):
            self.save()
    @staticmethod
    def get_mail_confirm(email):
        try:
            getmail=Customer.objects.get(email=email)
            return getmail
        except:
            return False
