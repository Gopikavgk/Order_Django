from django.test import TestCase
from numpy import product
from .models import Order
#https://www.youtube.com/watch?v=QCGvh4qIHLk
#https://learndjango.com/tutorials/django-testing-tutorial
class BasicTest_Learning(TestCase):

    def test_api_order(self):
        import requests
        import json
        url = "http://127.0.0.1:8000/shoppig_app/"

        payload = json.dumps({
          "product_name": "Pedigre",
          "invoice_id": "DB123RS",
          "product_price": 134,
          "product_quantity": 34,
          "user_name": "Manu",
          "user_consumer": "Consumer"
        })
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        check_flag=True
        data_flag=True
        if (response.text):
            data_flag=True
        else:
            data_flag=False
        self.assertEquals(check_flag,data_flag)
    #Page Fetching Test
    def test_about_page_status_code(self):
        response = self.client.get('http://127.0.0.1:8000/shoppig_app/savedborders?product_name=Cibaca&product_price=100&product_quantity=10&invoice_id=QWER123&user_name=John&user_consumer=Consumer')
        print("Response Fetched")
        print(response)
        #self.assertEquals(response.status_code, 200)
        self.assertContains(response, "<h2>Product Inserted. Enter New Products</h2>")


