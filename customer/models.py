from django.db import models
from bookadd.models import Books
from django.contrib.auth.models import User
from datetime import timedelta,datetime

# Create your models here.

class Carts(models.Model):
    product=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    options=(
        ("incart","incart"),
        ("orderplaced","orderplaced"),
        ("cancelled","cancelled")

    )
    status=models.CharField(max_length=20,choices=options,default="incart")
class Orders(models.Model):
    product=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=123)
    date=models.DateTimeField(auto_now_add=True,null=True)
    edate=datetime.today()+timedelta(days=5)
    expected_delivary_date=models.DateTimeField(default=edate,null=True)
    options=(
        ("orderplaced","orderplaced"),
        ("dispatched","dispatched"),
        ("in_transit","in_transit"),
        ("delivered","delivered"),
        ("order_cancelled","order_cancelled")

    )
    status=models.CharField(max_length=20,choices=options,default="orderplaced")

class Reviews(models.Model):
    comment=models.CharField(max_length=200)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Books,on_delete=models.CASCADE,related_name="products")
    options=[
        ("2","2"),("2.5","2.5"),("3","3"),("3.5","3.5"),("4","4"),("4.5","4.5"),("5","5")
    ]
    rating=models.CharField(max_length=20,choices=options)
