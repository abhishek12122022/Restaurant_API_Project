from django.db import models
from MenuItemAPI.models import MenuItem
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('user', 'menu_item')
    
    def save(self, *args, **kwargs):
        if not self.price:
            self.price =self.quantity*self.menu_item.price
        return super().save(*args, **kwargs)
