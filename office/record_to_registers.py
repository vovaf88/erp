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
from .record_to_registers_functions import RecordToRegisters


def add_goods_to_stock(data):
    doc_id = data['doc']
    product_id = data['product']
    str_doc_id = data['id']
    count = data['count']
    summa = data['summa']

    doc = PurchaseOfGood.objects.get(pk=doc_id)
    product = Product.objects.get(pk=product_id)
    str_doc = StrOfTabPurchaseOfGood.objects.get(pk=str_doc_id)

    RecordToRegisters.create_record_stock(doc, str_doc, product, count)
    RecordToRegisters.create_record_cost(doc, str_doc, product, count, summa)

    record_of_settlements_with_partners = SettlementsWithPartners.objects.filter(doc=doc)
    print('this doc: ', record_of_settlements_with_partners)
    if not record_of_settlements_with_partners:
        RecordToRegisters.create_record_settlements(doc, summa, doc.partner)
    else:
        summa_str = record_of_settlements_with_partners[0].summa
        summa = float(summa_str) + float(summa)
        RecordToRegisters.update_record_settlements(doc, summa, doc.partner)


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

    # check remainder of product
    if remainder < count:
        return False
    if remainder == 0:
        cost_price = 0
    elif remainder == count:
        cost_price = full_price
    else:
        cost_price = full_price / remainder * count

    RecordToRegisters.create_record_stock(doc, str_doc, product, -count)
    RecordToRegisters.create_record_cost(doc, str_doc, product, -count, -cost_price)
    RecordToRegisters.create_record_revenue(doc, str_doc, product, count, summa)

    record_of_settlements_with_partners = SettlementsWithPartners.objects.filter(doc=doc)
    print('this doc: ', record_of_settlements_with_partners)
    if not record_of_settlements_with_partners:
        RecordToRegisters.create_record_settlements(doc, -summa, doc.partner)
    else:
        summa_str = record_of_settlements_with_partners[0].summa
        summa = float(summa_str) - float(summa)
        RecordToRegisters.update_record_settlements(doc, summa, doc.partner)

    return True


def increase_our_credit(bank_doc):
    doc = MoneyOnBank.objects.get(id=bank_doc['id'])
    summa = float(bank_doc['summa'])
    partner = Partner.objects.get(id=bank_doc['partner'])
    RecordToRegisters.create_record_settlements(doc, summa, partner)


def decrease_our_credit(bank_doc):
    doc = MoneyOffBank.objects.get(id=bank_doc['id'])
    summa = -float(bank_doc['summa'])
    partner = Partner.objects.get(id=bank_doc['partner'])
    RecordToRegisters.create_record_settlements(doc, summa, partner)


def update_our_credit(bank_doc, doc_pk):
    if bank_doc['operation'] == 'Bank_off':
        doc = MoneyOffBank.objects.get(id=doc_pk)
        summa = -float(bank_doc['summa'])
        partner = Partner.objects.get(id=bank_doc['partner'])
        RecordToRegisters.update_record_settlements(doc, summa, partner)
    elif bank_doc['operation'] == 'Bank_on':
        doc = MoneyOnBank.objects.get(id=doc_pk),
        summa = float(bank_doc['summa']),
        partner = Partner.objects.get(id=bank_doc['partner'])
        RecordToRegisters.update_record_settlements(doc, summa, partner)


def update_str_sale(instance, request):
    data = request.data
    count = float(data['count'])
    price = float(data['price'])
    summa = float(data['summa'])
    doc = SaleOfGood.objects.get(id=data['doc'])
    product = Product.objects.get(id=data['product'])
    str_doc = StrOfTabSaleOfGood.objects.get(id=instance.id)
    old_sum = str_doc.summa

    RecordToRegisters.update_record_tab_sale_of_good(doc,
                                                     -count,
                                                     price,
                                                     summa,
                                                     product,
                                                     instance.id)
    RecordToRegisters.update_record_remaining_stock(doc,
                                                    str_doc,
                                                    product,
                                                    -count,
                                                    instance_id)

    cost_summ_count = CostOfGoods.objects.filter(product=product).aggregate(sum_prod=Sum("summa"),
                                                                            count_prod=Sum("count"))
    remainder = float(cost_summ_count['count_prod'])
    full_price = float(cost_summ_count['sum_prod'])

    # check remainder of product
    if remainder < count:
        return False
    if remainder == 0:
        cost_price = 0
    elif remainder == count:
        cost_price = full_price
    else:
        cost_price = full_price / remainder * count

    RecordToRegisters.update_record_cost(doc,
                                         product,
                                         str_doc,
                                         -count,
                                         -cost_price,
                                         instance.id)
    RecordToRegisters.update_record_revenue(doc,
                                            product,
                                            str_doc,
                                            count,
                                            summa,
                                            instance_id)

    record_of_settlements_with_partners = SettlementsWithPartners.objects.filter(doc=doc)
    summa_str = record_of_settlements_with_partners[0].summa
    summa_settlements = float(summa_str)-float(old_sum)+float(summa)

    RecordToRegisters.update_record_settlements(doc,
                                                summa_settlements,
                                                doc.partner)


def update_str_purchase(instance, request):
    data = request.data
    count = float(data['count'])
    price = float(data['price'])
    summa = float(data['summa'])
    doc = PurchaseOfGood.objects.get(id=data['doc'])
    product = Product.objects.get(id=data['product'])
    str_doc = StrOfTabPurchaseOfGood.objects.get(id=instance.id)
    old_sum = str_doc.summa

    RecordToRegisters.update_record_tab_purchase(doc,
                                                 product,
                                                 count,
                                                 price,
                                                 summa,
                                                 instance.id)

    RecordToRegisters.update_record_cost(doc,
                                         product,
                                         str_doc,
                                         count,
                                         summa,
                                         instance.id)

    record_of_settlements_with_partners = SettlementsWithPartners.objects.filter(doc=doc)
    summa_str = record_of_settlements_with_partners[0].summa
    summa_tab = float(summa_str)-float(old_sum)+float(summa)

    RecordToRegisters.update_record_settlements(doc,
                                                summa_tab,
                                                doc.partner)
    RecordToRegisters.update_record_remaining_stock(doc,
                                                    str_doc,
                                                    product,
                                                    count,
                                                    instance.id)

