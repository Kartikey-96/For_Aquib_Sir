from rest_framework import serializers
from .models import product , ProductReviewModel

class product_serializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = "__all__"

class productReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model =      ProductReviewModel
        fields = "__all__"   