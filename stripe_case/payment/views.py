import os
import sys
import stripe
import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dotenv import load_dotenv
from payment.models import Item, Order


load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    '%(asctime)s, %(lineno)d, %(levelname)s, %(message)s, %(funcName)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', default='')


@api_view(['GET', ])
def buy(request, price_id=None):
    items = price_id.split('-')
    line_items = [{"price": price_id, "quantity": 1} for price_id in items]
    sessions_response = 0
    stripe.api_key = STRIPE_SECRET_KEY
    try:
        sessions_response = stripe.checkout.Session.create(
            success_url="https://www.google.com/",
            line_items=line_items,
            mode="subscription", )
        if sessions_response:
            return redirect(sessions_response.url, code=303)
    except Exception as error:
        logger.error(f'Failed to get checkout.Session {error}')
        return Response(
            {'error': error},
            status=status.HTTP_400_BAD_REQUEST)


def item_detail(request, item_id=None):
    template = 'payment/items.html'
    stripe.api_key = STRIPE_SECRET_KEY
    item = get_object_or_404(Item, id=item_id)
    try:
        price_obj = stripe.Price.search(
            query=f"active:'true' AND product:'{item.price}'")

        price_id = price_obj['data'][0]['id']
        price = price_obj['data'][0]['unit_amount']
        valute = price_obj['data'][0]['currency']
        price = f'{price/100} {valute}'

        logger.debug('Get Price obj done')
    except Exception as error:
        logger.error(f'Failed to get Price {error}')
        html = f'<html><body>Failed to get Price {error} </body></html>'
        return HttpResponse(html)

    context = {
        'item': item,
        'price': price,
        'price_id': price_id, }
    return render(request, template, context)


def order_detail(request, order_id=None):
    template = 'payment/orders.html'
    stripe.api_key = STRIPE_SECRET_KEY
    order = get_object_or_404(Order, id=order_id)

    order_items_name = []
    total_price = 0
    price_id_list = []
    for item in order.items.all():
        try:
            price_obj = stripe.Price.search(
                query=f"active:'true' AND product:'{item.price}'")

            price_id_list.append(price_obj['data'][0]['id'])
            total_price += price_obj['data'][0]['unit_amount']
            order_items_name.append(item.name)
            valute = price_obj['data'][0]['currency']
            logger.debug('Get Price obj done')
        except Exception as error:
            logger.error(f'Failed to get Price {error}')
            html = f'<html><body>Failed to get Price {error} </body></html>'
            return HttpResponse(html)

    price_id = '-'.join(price_id_list)
    price = f'{total_price/100} {valute}'
    context = {
        'order_items_name': order_items_name,
        'price': price,
        'price_id': price_id, }
    return render(request, template, context)
