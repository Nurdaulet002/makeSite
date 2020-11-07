from django.db import models

# Base mixin
class BaseMixin(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


# список категории
class Category(BaseMixin):
    pass


# список товаров
class Good(BaseMixin):
    price = models.DecimalField(max_digits=5, decimal_places=2)
    top = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=30, default='Описание')
    detail = models.TextField(max_length=30, default='Подробности')
    Shipping_Returns = models.TextField(max_length=30, default='Доставка и Возврат')			