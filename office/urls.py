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
                    PartnerBankAccountAPIList,
                    PartnerBankAccountAPIDetail,
                    PartnerBankAccountAPIUpdate,
                    MyBankAccountAPIDetail,
                    MyBankAccountAPIList,
                    MyBankAccountAPIUpdate,
                    BankAPIList,
                    BankAPIDetail,
                    BankAPIUpdate,
                    Mytestdoc1DetailView,
                    Mytestdoc1ListView,
                    Mytesttab1CreateView,
                    PurchaseOfGoodListView,
                    PurchaseOfGoodDetailView,
                    StrOfTabPurchaseOfGoodCreateView,
                    SaleOfGoodListView,
                    SaleOfGoodDetailView,
                    StrOfTabSaleOfGoodCreateView,
                    )


urlpatterns = [
    path('products/', ProductAPIList.as_view(), name="products-list"),
    path('products/<int:pk>/', ProductAPIDetail.as_view()),
    path('productupdate/<int:pk>/', ProductAPIUpdate.as_view()),

    path('product-categories/', ProductCategoryAPIList.as_view()),
    path('measureunits/', MeasureUnitAPIList.as_view()),

    path('partners/', PartnerAPIList.as_view()),
    path('partners/<int:pk>/', PartnerAPIDetail.as_view()),
    path('partnerupdate/<int:pk>/', PartnerAPIUpdate.as_view()),

    path('mycompany/<int:pk>/', MyCompanyAPIUpdate.as_view()),

    path('banks/', BankAPIList.as_view()),
    path('banks/<int:pk>/', BankAPIDetail.as_view()),
    path('bankupdate/<int:pk>/', BankAPIUpdate.as_view()),

    path('mybankaccounts/', MyBankAccountAPIList.as_view()),
    path('mybankaccounts/<int:pk>/', MyBankAccountAPIDetail.as_view()),
    path('mybankaccountupdate/<int:pk>/', MyBankAccountAPIUpdate.as_view()),

    path('partnerbankaccounts/', PartnerBankAccountAPIList.as_view()),
    path('partnerbankaccounts/<int:pk>/', PartnerBankAccountAPIDetail.as_view()),
    path('partnerbankaccountupdate/<int:pk>/', PartnerBankAccountAPIUpdate.as_view()),

    path('docs/', Mytestdoc1ListView.as_view()),
    path('docs/<int:pk>/', Mytestdoc1DetailView.as_view()),
    path('tabscreate/', Mytesttab1CreateView.as_view()),

    path('purchase/', PurchaseOfGoodListView.as_view()),
    path('purchase/<int:pk>', PurchaseOfGoodDetailView.as_view()),
    path('tabpurchasecreate/', StrOfTabPurchaseOfGoodCreateView.as_view()),

    path('sale/', SaleOfGoodListView.as_view()),
    path('sale/<int:pk>', SaleOfGoodDetailView.as_view()),
    path('tabsalecreate/', StrOfTabSaleOfGoodCreateView.as_view()),

]


