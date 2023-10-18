from django.db import models
from apps.core.basemodel import Basemodel
from django.utils.translation import gettext_lazy as _
# class Category(Basemodel):
#     name = models.CharField(max_length=255)
#
#     class Meta:
#         verbose_name_plural = 'Categories'
#
#     def __str__(self):
#         return self.name


class Inventory(Basemodel):
    # name = models.CharField(max_length=255)
    # description = models.TextField(blank=True)
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # quantity = models.IntegerField(default=0)
    # price = models.DecimalField(max_digits=8, decimal_places=2)
    # manufacturer = models.CharField(max_length=255)

    id = models.CharField(max_length=10, primary_key=True)
    product_name = models.CharField(_("Product Name"), max_length=100)
    description = models.TextField(_("Description"), null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("Price"))
    category = models.CharField(_("Category"), max_length=25, null=True, blank=True)
    instock_quantity = models.CharField(_("Instock Quantity"), max_length=50)
    # amount = models.CharField(_("Amount"), null=True, blank=True, max_length=100)
    # ingredients = models.CharField(_("Ingredients"), null=True, blank=True, max_length=100)
    # use = models.CharField(_("Suggested Use"), null=True, blank=True, max_length=100)

    def save(self, *args, **kwargs):
        if not self.id:
            last_order = Inventory.objects.order_by('-id').first()
            if last_order:
                last_id = int(last_order.id.split('-')[1])
            else:
                last_id = 0
            self.id = f'PROD-{str(last_id + 1).zfill(4)}'
        super().save(*args, **kwargs)



    class Meta:
        verbose_name = _("Inventory")
        verbose_name_plural = _("Inventories")
        ordering = ['-created_on']







