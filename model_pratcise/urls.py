from django.urls import path
from model_pratcise import views


urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('index/',views.index,name="index"),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

    path('customer_list/',views.customer_list,name="customer_list"),
    path('customer_edit/<int:id>',views.customer_edit,name="customer_edit"),
    path('customer_update/<int:id>',views.customer_update,name="customer_update"),
    path('customer_delete/<int:id>',views.customer_delete,name="customer_delete"),
    path('customer_detail/<int:id>',views.customer_detail,name="customer_detail"),
    
    path('order_detail/',views.order_detail,name='order_detail'),
    path('order_list/',views.order_list,name='order_list'),
    path('order_edit/<int:id>',views.order_edit,name='order_edit'),
    path('order_update/<int:id>',views.order_update,name='order_update'),
    path('order_delete/<int:id>',views.order_delete,name='order_delete'),

   
    

]
