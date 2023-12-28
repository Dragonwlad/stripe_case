import os
import stripe
import json
from dotenv import load_dotenv


load_dotenv()

stripe.api_key = os.getenv('STRIPE_SECRET_KEY', default='')

# list customers
# customers = stripe.Customer.list()

# # print the first customer's email
# print(customers.data[0].email)

# retrieve specific Customer
# customer = stripe.Customer.retrieve("cus_PFhxPbpYkV6sLk")

# # print that customer's email
# print(customer)

# balance = stripe.Balance.retrieve()

# Создаем продукт
# stripe.Product.create(name="Platinum Plan")


# # Создаем цену для продукта
# price = stripe.Price.create(
#     currency="usd",
#     unit_amount=100,
#     recurring={"interval": "month"},
#     product_data={"name": "Platinum Plan"},
#     )
# print(f'----------{price}')

# получить цены
# prices = stripe.Price.list()
# print(f'prices===={prices}')

# product_price_json = stripe.Price.search(
#     query="active:'true' AND product:'prod_PG69iYfCwYb4Ef'")
# product_price = product_price_json['data'][0]

# print(f'product_price===={product_price}')

# print('---------', type(product_price))
# # product_price_data = product_price.get('data')
# # print(f'product_price===={product_price_data}')
# price = product_price['unit_amount']
# valute = product_price['currency']
# print(f'{price} ===={valute}')

# Получить продукты
# prouducts = stripe.Product.list()
# print(f'prouducts===={prouducts}')

# prices_product = stripe.Product.retrieve("prod_PFjIkZG70E5vyH")
# print(f'prices_product===={prices_product}')

# То что нужно для тестового checkout.Session.create
# price_id_1 = 'price_1ORDqCCYPnFtEVe4rg1mxlY3' # из url получили id
# price_id_2 = 'price_1ORaErCYPnFtEVe4xL8tuADp' # из url получили id

# quantity = 1
# sessions_response = stripe.checkout.Session.create(
#     success_url="https://www.google.com/",
#     line_items=[{"price": price_id_1, "quantity": quantity},
#                 {"price": price_id_2, "quantity": quantity}],
#     mode="subscription",
#     )
# print(f'sessions_id===={sessions_response}')
# sessions_id = sessions_response['id']
# print(f'sessions_id===={sessions_id}')

# Декативировал лишние продукты
# stripe.Product.modify("prod_PFjCgr68RvlND6", active=False)


# stripe.Product.modify("prod_PFj61c7qN6MMBO", active=False)

price_id = 'price_1ORDqCCYPnFtEVe4rg1mxlY3-price_1ORZx5CYPnFtEVe4kz0C8ZpY'
items = price_id.split('-')
line_items = [{"price": i, "quantity": 1} for i in items]
print(line_items)
