from .models import StrOfTabPurchaseOfGood, RemainingStock, PurchaseOfGood, Product

#{'id': 6, 'count': '2.000', 'price': '20.00', 'summa': '40.00', 'doc': 1, 'product': 10}


def add_goods_to_stock(data):
    doc_id = data['doc']
    product_id = data['product']
    str_doc_id = data['id']
    count = data['count']

    doc = PurchaseOfGood.objects.get(pk=doc_id)
    product = Product.objects.get(pk=product_id)
    str_doc = StrOfTabPurchaseOfGood.objects.get(pk=str_doc_id)

    RemainingStock.objects.create(
        doc=doc,
        str_doc=str_doc,
        product=product,
        count=count,
    )

