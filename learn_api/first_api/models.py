from django.db import models



class product(models.Model):
    id = models.UUIDField(primary_key=True , )
    title = models.TextField(max_length=200)
    name = models.CharField(max_length=50)
    descripition = models.TextField(max_length=200)


class ProductReviewModel(models.Model):
    product_id = models.IntegerField()
    review_id = models.IntegerField()
    user_id = models.IntegerField()
    comment = models.CharField(max_length=8000)
    rating = models.DecimalField(max_digits=4 , decimal_places= 2)
