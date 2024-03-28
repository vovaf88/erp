from django.db.models import Count, Case, When, Avg, Sum
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


def add_goods_to_stock(data):
    doc_id = data['doc']
    product_id = data['product']
    str_doc_id = data['id']
    count = data['count']
    summa = data['summa']

    doc = PurchaseOfGood.objects.get(pk=doc_id)
    product = Product.objects.get(pk=product_id)
    str_doc = StrOfTabPurchaseOfGood.objects.get(pk=str_doc_id)

    RemainingStock.objects.create(
        doc=doc,
        str_doc=str_doc,
        product=product,
        count=count,
    )

    CostOfGoods.objects.create(
        doc=doc,
        str_doc=str_doc,
        product=product,
        count=count,
        summa=summa
    )

    SettlementsWithPartners.objects.create(
        doc=doc,
        summa=summa,
        partner=doc.partner
    )


def remove_goods_from_stock(data):
    doc_id = data['doc']
    product_id = data['product']
    str_doc_id = data['id']
    count = float(data['count'])
    summa = float(data['summa'])

    doc = SaleOfGood.objects.get(pk=doc_id)
    product = Product.objects.get(pk=product_id)
    str_doc = StrOfTabSaleOfGood.objects.get(pk=str_doc_id)

    cost_summ_count = CostOfGoods.objects.filter(product=product).aggregate(sum_prod=Sum("summa"),
                                                                            count_prod=Sum("count"))
    remainder = float(cost_summ_count['count_prod'])
    full_price = float(cost_summ_count['sum_prod'])

    print('remainder= ', remainder, ', full_price= ', full_price, ', count= ', count, ', summa=', summa)

    # check remainder of product
    if remainder < count:
        return False
    if remainder == 0:
        cost_price = 0
    elif remainder == count:
        cost_price = full_price
    else:
        cost_price = full_price / remainder * count

    RemainingStock.objects.create(
        doc=doc,
        str_doc=str_doc,
        product=product,
        count=-count,
    )

    CostOfGoods.objects.create(
        doc=doc,
        str_doc=str_doc,
        product=product,
        count=-count,
        summa=-cost_price
    )

    Revenue.objects.create(
        doc=doc,
        str_doc=str_doc,
        product=product,
        count=count,
        summa=summa
    )

    SettlementsWithPartners.objects.create(
        doc=doc,
        summa=-summa,
        partner=doc.partner
    )

    return True


def increase_our_credit(bank_doc):
    # {'id': 4, 'number': '3', 'doc_date': '2024-03-24T16:30:00Z', 'summa': '1000.00', 'operation': 3, 'my_company': 1, 'partner': 6}
    SettlementsWithPartners.objects.create(
        doc=MoneyOnBank.objects.get(id=bank_doc['id']),
        summa=float(bank_doc['summa']),
        partner=Partner.objects.get(id=bank_doc['partner'])
    )


def decrease_our_credit(bank_doc):
    SettlementsWithPartners.objects.create(
        doc=MoneyOffBank.objects.get(id=bank_doc['id']),
        summa=-float(bank_doc['summa']),
        partner=Partner.objects.get(id=bank_doc['partner'])
    )


def update_our_credit(bank_doc, doc_pk):

    # <QueryDict: {'number': ['1'], 'doc_date': ['2024-03-19T22:34'], 'operation': ['Bank_off'], 'my_company': ['1'], 'partner': ['1'], 'summa': ['400']}> 12

    if bank_doc['operation'] == 'Bank_off':
        SettlementsWithPartners.objects.filter(doc__id=doc_pk).update(
            doc=MoneyOffBank.objects.get(id=doc_pk),
            summa=-float(bank_doc['summa']),
            partner=Partner.objects.get(id=bank_doc['partner'])
        )
    elif bank_doc['operation'] == 'Bank_on':

        SettlementsWithPartners.objects.filter(doc__id=doc_pk).update(
            doc=MoneyOnBank.objects.get(id=doc_pk),
            summa=float(bank_doc['summa']),
            partner=Partner.objects.get(id=bank_doc['partner'])
        )


def update_str_sale(instance, request):
    pass


def update_str_purchase(instance, request):
    pass