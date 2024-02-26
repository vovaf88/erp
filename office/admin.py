from django.contrib import admin
from .models import Product, ProductCategory, MeasureUnit, MyCompany, Partner


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(MeasureUnit)

admin.site.register(MyCompany)
admin.site.register(Partner)



