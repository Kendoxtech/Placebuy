from django.db import models
from datetime import datetime


class Seller(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    address = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    website = models.URLField(default='')

    def __str__(self):
        return self.name


class Condition(models.Model):
    condition = {
        'New': 'New',
        'Old': 'Old',
        'Damaged': 'Damaged'
    }

    condition = models.CharField(max_length=7, choices=condition)

    def __str__(self):
        return self.condition


class Category(models.Model):
    category = {
        'Electronics': 'Electronics',
        'Furniture': 'Furniture',
        'Books': 'Books',
        'Phones and Tablets': 'Phones and Tablets',
        'Laptop': 'Laptop',
        'Camera': 'Camera',
        'Home Appliances': 'Home Appliances',
        'Clothing': 'Clothing'

    }
    category = models.CharField(max_length=50, null=True, choices=category)

    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = 'Categories'


class ProductImage(models.Model):
    images = models.ImageField(upload_to="product_image", default="product.jpg")
    date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ForeignKey(ProductImage, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Amount(models.Model):
    amount = models.FloatField()

    def __str__(self):
        return str(self.amount)



class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.ForeignKey(Amount, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    discount = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return str(self.discount)




class Payment_method(models.Model):
    payment_method = {
        'Cash': 'Cash',
        'Paypal': 'Paypal',
        'Card': 'Card',
        'Bank': 'Bank'
    }

    payment_method = models.CharField(max_length=10, choices=payment_method)

    def __str__(self):
        return self.payment_method


class Payment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.ForeignKey(Amount, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(Payment_method, on_delete=models.CASCADE)


class Quantity(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.quantity)


class Order_date(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __str__(self):
        return str(self.datetime)


class Status(models.Model):
    status_name = {
        'Processing': 'Processing',
        'Processed': 'Processed',
        'Out for Delivery': 'Out for Delivery',
        'In Transit': 'In Transit',
        'Delivered': 'Delivered'
    }

    status_name = models.CharField(max_length=20, choices=status_name)

    def __str__(self):
        return str(self.status_name)


class Order_status(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.status)


class Buyer(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    payment_method = models.ForeignKey(Payment_method, on_delete=models.CASCADE)

    def __str__(self):
        return self.name





class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, max_length=255)
    price = models.ForeignKey(Price, null=True, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity, null=True, on_delete=models.CASCADE)
    order_date = models.ForeignKey(Order_date, on_delete=models.CASCADE)
    order_status = models.ForeignKey(Order_status, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(Payment_method, on_delete=models.CASCADE, max_length=255)
    amount = models.ForeignKey(Amount, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)


class Transaction_status(models.Model):
    status = {
        'Processing': 'Processing',
        'Pending': 'Pending',
        'Successful': 'Successful',
        'Unsuccessful': 'Unsuccessful'
    }
    payment_method = models.ForeignKey(Payment_method, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=status)

    def __str__(self):
        return str(self.status)


class Transaction(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)
    amount = models.ForeignKey(Amount, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(Payment_method, on_delete=models.CASCADE)
    datetime = models.ForeignKey(Order_date, on_delete=models.CASCADE)
    status = models.ForeignKey(Transaction_status, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    time = models.TimeField()
    datetime = models.DateField()


class Message(models.Model):
    buyer = models.ForeignKey(Buyer, null=True, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    time = models.TimeField()
    datetime = models.DateField()
