from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import DateInput

# Create your models here.

class Ticket(models.Model):
    state_choices = [
        ('Punjab','Punjab'),
        ('Gujrat','Gujrat'),
        ('Mumbai','Mumbai'),
        ('Karnataka','Karnataka'),
    ]
    user =models.CharField(max_length=150)
    full_name = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(4),MinValueValidator(1)])
    source = models.CharField(max_length=50,choices=state_choices)
    destination = models.CharField(max_length=50,choices=state_choices)
    booking_date = models.DateField()

    def __str__(self):
        return self.full_name

class Offer(models.Model):
    title = models.CharField(max_length=100)
    discount_price = models.IntegerField()
    actual_price = models.IntegerField()
    descriptions = models.TextField(max_length=300)
    offer_image = models.ImageField(upload_to = 'offerimg')

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.username)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    message = models.CharField(max_length=250)
    date = models.DateField(auto_now=True)

class Food(models.Model):
    title = models.CharField(max_length=100)
    actual_price = models.IntegerField()
    descriptions = models.TextField(max_length=300)
    quantity = models.PositiveIntegerField()
    food_image = models.ImageField(upload_to = 'foodimg')

class Profile(models.Model):
    state_choices = [
        ('Punjab','Punjab'),
        ('Gujrat','Gujrat'),
        ('Mumbai','Mumbai'),
        ('Karnataka','Karnataka'),
    ]
    name = models.CharField(max_length=50)
    addr1 = models.CharField(max_length=400)
    addr2 = models.CharField(max_length=400)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50,choices=state_choices)
    zipcode = models.IntegerField()


class Register_table(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.IntegerField()
    profile_pic = models.ImageField(upload_to="profile_pic",null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    about = models.TextField(max_length=250,null=True,blank=True)
    gender = models.CharField(max_length=200,null=True,blank=True,default="Male")
    occupation = models.CharField(max_length=200,null=True,blank=True)
    added_on = models.DateField(auto_now_add=True,null=True,blank=True)
    uploaded_on = models.DateField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return str(self.user.username)
