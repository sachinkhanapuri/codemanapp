from django.urls import path
from basicform import views

urlpatterns = [
    path('',views.customer_form,name="customer_form"),
    path('index1',views.index1,name='index1'),
    path('customer_list1',views.customer_list1,name='customer_list1'),
    path('customer_edit1/<int:id>',views.customer_edit1,name='customer_edit1'),
    path('customer_update1/<int:id>',views.customer_update1,name='customer_update1'),
]