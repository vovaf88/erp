from django.urls import path
from .views import (ProductAPIList,
                    ProductAPIDetail,
                    ProductAPIUpdate,
                    ProductCategoryAPIList,
                    MeasureUnitAPIList,
                    PartnerAPIList,
                    PartnerAPIDetail,
                    PartnerAPIUpdate,
                    MyCompanyAPIUpdate,
                    )


urlpatterns = [
    path('products/', ProductAPIList.as_view()),
    path('products/<int:pk>/', ProductAPIDetail.as_view()),
    path('productupdate/<int:pk>/', ProductAPIUpdate.as_view()),
    path('product-categories/', ProductCategoryAPIList.as_view()),
    path('measureunits/', MeasureUnitAPIList.as_view()),

    path('partners/', PartnerAPIList.as_view()),
    path('partners/<int:pk>/', PartnerAPIDetail.as_view()),
    path('partnerupdate/<int:pk>/', PartnerAPIUpdate.as_view()),

    path('mycompany/<int:pk>/', MyCompanyAPIUpdate.as_view()),

]


