from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Products,Order
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def formm(request):
    return render(request,"orders.html")

def savedborders(request):
    product_name=request.GET.get('product_name')
    print(product_name)
    product_price=request.GET.get('product_price')
    print(product_price)
    product_quantity=request.GET.get('product_quantity')
    print(product_quantity)
    invoice_id=request.GET.get('invoice_id')
    print(invoice_id)
    user_name=request.GET.get('user_name')
    print(user_name)
    user_consumer=request.GET.get('user_consumer')
    print(user_consumer)
    order_data={
            'product_name':product_name,
            'Invoice_ID':invoice_id,
            'product_price':product_price,
            'product_quantity':product_quantity,
            'user_name':user_name,
            'user_consumer':user_consumer
    }
    cart_item=Order.objects.create(**order_data)
    data={
            "status":f"New item added to Cart with id:{cart_item.id}"
    }
    print(data)
    return render(request,"orders.html",{'flag': 'Product Inserted. Enter New Products'})
    return HttpResponse("Data Saved Macha")

@method_decorator(csrf_exempt,name='dispatch')
class Products1(View):
    def post(self,request):
        data=json.loads(request.body.decode("utf-8"))
        print(data)
        p_name=data.get('product_name')
        p_price=data.get('product_price')
        p_qty=data.get('product_quantity')
        product_data={
            'product_name':p_name,
            'product_price':p_price,
            'product_quantity':p_qty,
        }
        cart_item=Products.objects.create(**product_data)
        data={
            "status":f"New item added to Cart with id:{cart_item.id}"
        }
        return JsonResponse(data,status=201)

    def get(self, request):
        items_count = Products.objects.count()
        items = Products.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'product_name': item.product_name,
                'product_price': item.product_price,
                'product_quantity': item.product_quantity,
            })

        data = {
            'items': items_data,
            'count': items_count,
        }

        return JsonResponse(data)    


@method_decorator(csrf_exempt,name='dispatch')
class Mycart1(View):
    def post(self,request):
        data=json.loads(request.body.decode("utf-8"))
        print(data)
        p_name=data.get('product_name')
        p_price=data.get('product_price')
        p_qty=data.get('product_quantity')
        invoice_id=data.get('invoice_id')
        user_name=data.get('user_name')
        user_consumer=data.get('user_consumer')

        order_data={
            'product_name':p_name,
            'Invoice_ID':invoice_id,
            'product_price':p_price,
            'product_quantity':p_qty,
            'user_name':user_name,
            'user_consumer':user_consumer
        }
        cart_item=Order.objects.create(**order_data)
        data={
            "status":f"New item added to Cart with id:{cart_item.id}"
        }
        return JsonResponse(data,status=201)
