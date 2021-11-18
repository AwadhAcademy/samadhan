from django.db import models

# Create your models here.
class quote_data(models.Model):
    fname = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100 ,default="abc@gmail.com")
    quary= models.CharField(max_length=100)

    def __str__(self):
        return self.fname
class Carousel_Data(models.Model):
    # name=models.CharField(max_length=50 , default="Undefined")
    photo= models.ImageField(upload_to="base/images",default="")
    # def __str__(self):
    #     return name

class service(models.Model):
    heading = models.CharField(max_length=100)
    information = models.CharField(max_length=1000)
    icon= models.ImageField(upload_to="base/images",default="")
    def __str__(self):
        return self.heading

class legal_service(models.Model):
    heading = models.CharField(max_length=100)
    information = models.CharField(max_length=1000)
    icon= models.ImageField(upload_to="base/images",default="")
    def __str__(self):
        return self.heading

class tax_compliance(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100 ,default="abc@gmail.com")
    qurey= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class new_registration(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email = models.EmailField(max_length=100 ,default="abc@gmail.com")
    password1 = models.IntegerField()
    password2 = models.IntegerField()

    def __str__(self):
        return self.name

class bloging_data(models.Model):
    heading=models.CharField(max_length=100)
    information=models.CharField(max_length=5000)
    image= models.ImageField(upload_to="base/images",default="")
    hyper_link=models.CharField(max_length=100)
    def __str__(self):
        return self.heading

class additional_services(models.Model):
    heading = models.CharField(max_length=100)
    data = models.CharField(max_length=5000)
    points = models.CharField(max_length=10000)
    image= models.ImageField(upload_to="base/images",default="")
    def __str__(self):
        return self.heading