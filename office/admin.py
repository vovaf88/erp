from django.contrib import admin
from .models import (Product,
                     ProductCategory,
                     MeasureUnit,
                     MyCompany,
                     Partner,
                     Bank,
                     MyBankAccount,
                     PartnerBankAccount,
                     PurchaseOfGood,
                     StrOfTabPurchaseOfGood,
                     SaleOfGood,
                     StrOfTabSaleOfGood,
                     RemainingStock,
                     CostOfGoods,
                     SettlementsWithPartners,
                     MoneyOnBank,
                     MoneyOffBank,
                     )


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(MeasureUnit)

admin.site.register(MyCompany)
admin.site.register(Partner)

admin.site.register(Bank)
admin.site.register(MyBankAccount)
admin.site.register(PartnerBankAccount)

# Documents
admin.site.register(PurchaseOfGood)
admin.site.register(StrOfTabPurchaseOfGood)
admin.site.register(SaleOfGood)
admin.site.register(StrOfTabSaleOfGood)
admin.site.register(MoneyOnBank)
admin.site.register(MoneyOffBank)

# Registers
admin.site.register(RemainingStock)
admin.site.register(CostOfGoods)
admin.site.register(SettlementsWithPartners)

