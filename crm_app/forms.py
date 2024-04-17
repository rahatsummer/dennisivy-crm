from django.forms import ModelForm
from crm_app.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        # fields = '__all__'
        fields = ['customer', 'product',  'status']
