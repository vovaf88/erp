from django.urls import path
from .views import ProductAPIList, ProductAPIDetail, ProductAPIUpdate


urlpatterns = [
    path('productlist/', ProductAPIList.as_view()),
    path('productdetail/<int:pk>/', ProductAPIDetail.as_view()),
    path('productupdate/<int:pk>/', ProductAPIUpdate.as_view()),
]
