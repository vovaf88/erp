from django.contrib import admin
from .models import (Product,
                     ProductCategory,
                     MeasureUnit,
                     MyCompany,
                     Partner,
                     Bank,
                     MyBankAccount,
                     PartnerBankAccount,
                     Operation,
                     Mytestdoc1,
                     Mytesttab1
                     )


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(MeasureUnit)

admin.site.register(MyCompany)
admin.site.register(Partner)

admin.site.register(Bank)
admin.site.register(MyBankAccount)
admin.site.register(PartnerBankAccount)
admin.site.register(Operation)

admin.site.register(Mytestdoc1)
admin.site.register(Mytesttab1)
