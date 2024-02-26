from django.urls import path
from .views import ProductAPIList, ProductAPIDetail, ProductAPIUpdate, ProductCategoryAPIList, MeasureUnitAPIList


urlpatterns = [
    path('products/', ProductAPIList.as_view()),
    path('products/<int:pk>/', ProductAPIDetail.as_view()),
    path('productupdate/<int:pk>/', ProductAPIUpdate.as_view()),
    path('product-categories/', ProductCategoryAPIList.as_view()),
    path('measureunits/', MeasureUnitAPIList.as_view()),
]


