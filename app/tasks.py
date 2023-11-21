from datetime import date
import json
import lzstring
from django.db import transaction
from celery import shared_task

from app.models import Orders, OrdersDetail


@shared_task
def save_orders_clients(compressedOrdersData):
    print(compressedOrdersData)
    compressor = lzstring.LZString()

    #En el BE descomprimir los datos con lzstring.
    orders_json = compressor.decompressFromBase64(compressedOrdersData)

    #convertir el JSON a tipo de datos python.
    client_orders = json.loads(orders_json)
    ultimo_pedido = Orders.objects.all()
    with transaction.atomic():
        try:
            for client_id, client_order_items in client_orders.items():
                numero_pedido = ultimo_pedido.pedido_numero + 1
                order = Orders(pedido_numero=numero_pedido,
                               pdvobj=client_id,
                               doc_tipo="dcotipo",
                               doc_fecha=date())
                for client_order in client_order_items:
                    order_detail = OrdersDetail(**client_order)
                    order_detail.orderobj = order.id
                    order_detail.save()
            transaction.commit()

        except Exception as e:
            transaction.rollback()
