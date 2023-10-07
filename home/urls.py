from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('service/',views.service,name='service'),
    path('coupon/<int:slot_id>/',views.coupon,name='coupon'),

    path('myorder/',views.myorder,name='myorder'),
    path('add_cart/<int:id>/',views.add_cart,name='add_cart'),
    path('view_cart/',views.view_cart,name='view_cart'),
    path('remove_cart/<int:id>/',views.remove_cart,name='remove_cart'),
    path('bookingview/<int:slot_id>/',views.bookingview,name='bookingview'),
    
    path('orderdetails/<int:id>/',views.orderdetails,name='orderdetails'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('editprofile/<int:id>/',views.editprofile,name='editprofile'),
    path('category/<str:vehicle>/',views.category,name='category'),
    path('select/<int:id>/',views.select,name='select'),
    path('slotbook/<int:id>/',views.slotbook,name='slotbook'),
    # path('slotbook/<str:dates>/',views.slotbook,name='slotbookk'),
    path('slotbook/<int:id>/<str:dates>/',views.slotbook,name='slotbookkk'),
    path('booking/<int:slot_id>/',views.book,name='booking'),
    path('booking/<int:slot_id>/<str:coupon>/', views.book, name='bookking'),
    path('order/download_invoice/<int:booking_id>/', views.download_invoice, name='download_invoice'),


    
    
    
    
    
]
