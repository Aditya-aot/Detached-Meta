from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view , name='home_view') , 
    path('detail/<str:pk>', views.detail_view , name='detail_view'),
    path('product', views.product_page_view , name='product_page_view') ,
    path('download_confirm/<str:order>/<str:pk>', views.download_confirm_view , name='download_confirm_view') ,

]