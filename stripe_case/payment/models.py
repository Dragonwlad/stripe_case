from django.db import models

MAX_LEN_ITEM_NAME = 100
MAX_PRICE_LEN = 50


class Item(models.Model):
    name = models.CharField(max_length=MAX_LEN_ITEM_NAME)
    description = models.TextField()
    price = models.CharField(max_length=MAX_PRICE_LEN)

    class Meta():
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)
