from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return '{0:.2f}'.format(self.price / 100)


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name='orders', through='OrderPositions')

    def get_price_cents(self):
        total_coast = 0
        for position in self.positions.all():
            coast = position.item.price * position.qty
            total_coast += coast
        return total_coast

    def get_display_price(self):
        total = self.get_price_cents()
        return '{0:.2f}'.format(total / 100)


class OrderPositions(models.Model):
    item = models.ForeignKey(Item, related_name='positions', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='positions', on_delete=models.CASCADE)
    qty = models.IntegerField()
