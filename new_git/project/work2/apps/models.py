from django.db import models

# Create your models here.
class Registration(models.Model):
    username=models.CharField(max_length=15,unique=True)
    email=models.EmailField()
    phoneno=models.CharField(max_length=10)
    password=models.CharField(max_length=15)

    def __str__(self):
        return self.username

class Productdetails(models.Model):
    product_name=models.CharField(max_length=15)
    product_price=models.IntegerField()
    product_image=models.FileField()
    description=models.CharField(max_length=100)
    product_stock=models.IntegerField(default=1)
    category=models.CharField(max_length=20)

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user_details=models.ForeignKey(Registration,on_delete=models.CASCADE)
    product_details=models.ForeignKey(Productdetails,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)


class Wishlist(models.Model):
    user_details = models.ForeignKey(Registration, on_delete=models.CASCADE)
    product_details = models.ForeignKey(Productdetails, on_delete=models.CASCADE)

class PasswordReset(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE)
    token=models.CharField(max_length=10)

class deliverydetails(models.Model):
    userdetails=models.ForeignKey(Registration,on_delete=models.CASCADE)
    productdetails_2=models.ForeignKey(Productdetails,on_delete=models.CASCADE)
    Fullname=models.CharField(max_length=20)
    Pincode=models.CharField(max_length=10)
    state=models.CharField(max_length=15)
    Address=models.CharField(max_length=40)
    city = models.CharField(max_length=15)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()
    payment_status = models.CharField(max_length=20, null=True,default='TRUE')
    purchase_date = models.DateTimeField(auto_now=True, null=True)
    product_status = models.CharField(max_length=50, null=True, default='Order placed')
    instruction = models.CharField(max_length=50, null=True, default='Your Order Has Been Successfully Placed')
    ORDER_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('delivered', 'Delivered'),
        ('out_for_delivery', 'Out for Delivery'),
        ('pending', 'Pending'),
    ]







