from django.views import View
from django.shortcuts import render
from django.http import JsonResponse, Http404,HttpResponseBadRequest
from .data import coustmetr_Data
import json
from .serialazers import productReviewSerializer



book_review_data_Store = []

class ProductView(View):
    def get(self, request):
        return JsonResponse(coustmetr_Data, safe=False)

class ProductWithIdView(View):
    def get(self, request, customerId):
        found = None
        for data in coustmetr_Data:
            if data["id"] == customerId:
                found = data
                break

        if found:
            return JsonResponse(found, safe=False)
        else:
            return JsonResponse({"error": "Customer not found"}, status=404)
        

class ProductReviewView(View):
    def post(self, request, productId):
        review_data= json.loads(request.body)
        review_data["productId"] = productId
        review_data["review_id"] = len(book_review_data_Store)+1


        data_PassWith_Serializer = productReviewSerializer(data=review_data)
        if data_PassWith_Serializer.is_valid():
            book_review_data_Store.append(data_PassWith_Serializer)
            return JsonResponse(data_PassWith_Serializer.data, status=201)


