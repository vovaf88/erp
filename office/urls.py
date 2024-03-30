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
                    PurchaseOfGoodListView,
                    PurchaseOfGoodDetailView,
                    StrOfTabPurchaseOfGoodCreateView,
                    StrOfTabPurchaseOfGoodUpdateView,
                    SaleOfGoodListView,
                    SaleOfGoodDetailView,
                    StrOfTabSaleOfGoodCreateView,
                    StrOfTabSaleOfGoodUpdateView,
                    MoneyOffBankAPIList,
                    MoneyOffBankAPIDetail,
                    MoneyOffBankAPIUpdate,
                    MoneyOnBankAPIUpdate,
                    MoneyOnBankAPIList,
                    MoneyOnBankAPIDetail,
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

    path('purchase/', PurchaseOfGoodListView.as_view()),
    path('purchase/<int:pk>', PurchaseOfGoodDetailView.as_view()),
    path('tabpurchasecreate/', StrOfTabPurchaseOfGoodCreateView.as_view()),
    path('tabpurchaseupdate/<int:pk>/', StrOfTabPurchaseOfGoodUpdateView.as_view()),

    path('sale/', SaleOfGoodListView.as_view()),
    path('sale/<int:pk>', SaleOfGoodDetailView.as_view()),
    path('tabsalecreate/', StrOfTabSaleOfGoodCreateView.as_view()),
    path('tabsaleupdate/<int:pk>/', StrOfTabSaleOfGoodUpdateView.as_view()),

    path('moneyon/', MoneyOnBankAPIList.as_view()),
    path('moneyon/<int:pk>/', MoneyOnBankAPIDetail.as_view()),
    path('moneyonupdate/<int:pk>/', MoneyOnBankAPIUpdate.as_view()),

    path('moneyoff/', MoneyOffBankAPIList.as_view()),
    path('moneyoff/<int:pk>/', MoneyOffBankAPIDetail.as_view()),
    path('moneyoffupdate/<int:pk>/', MoneyOffBankAPIUpdate.as_view()),

]


