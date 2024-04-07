from .models import (StrOfTabPurchaseOfGood,
                     RemainingStock,
                     PurchaseOfGood,
                     Product,
                     CostOfGoods,
                     SettlementsWithPartners,
                     Revenue,
                     SaleOfGood,
                     StrOfTabSaleOfGood,
                     MoneyOnBank,
                     MoneyOffBank,
                     Partner)


class RecordToRegisters:
    @staticmethod
    def create_record_stock(doc, str_doc, product, count):
        RemainingStock.objects.create(
            doc=doc,
            str_doc=str_doc,
            product=product,
            count=-count,
        )

    @staticmethod
    def create_record_cost(doc, str_doc, product, count, summa):
        CostOfGoods.objects.create(
            doc=doc,
            str_doc=str_doc,
            product=product,
            count=count,
            summa=summa
        )

    @staticmethod
    def create_record_revenue(doc, str_doc, product, count, summa):
        Revenue.objects.create(
            doc=doc,
            str_doc=str_doc,
            product=product,
            count=count,
            summa=summa
        )

    @staticmethod
    def create_record_settlements(doc, summa, partner):
        SettlementsWithPartners.objects.create(
            doc=doc,
            summa=summa,
            partner=partner
        )

    @staticmethod
    def update_record_settlements(doc, summa, partner):
        SettlementsWithPartners.objects.filter(doc=doc).update(
            doc=doc,
            summa=summa,
            partner=partner
        )

    @staticmethod
    def update_record_tab_sale_of_good(doc, count, price, summa, product, instance_id):
        StrOfTabSaleOfGood.objects.filter(pk=instance_id).update(
            count=count,
            price=price,
            summa=summa,
            doc=doc,
            product=product
        )
    @staticmethod
    def update_record_remaining_stock(doc, str_doc, product, count, instance_id):
        RemainingStock.objects.filter(pk=instance_id).update(
            doc=doc,
            str_doc=str_doc,
            product=product,
            count=-count,
        )