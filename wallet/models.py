from decimal import Decimal

from django.db import models
from django.utils import timezone
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from core.models import BaseModel

MOVEMENT_CHOICES = (
    ('INC', 'Income'),
    ('EXP', 'Expense'),
)


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Account(BaseModel):
    name = models.CharField(max_length=255)
    total = models.DecimalField(default=0.00, max_digits=14, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.total} - {self.user}"


class Movement(BaseModel):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(default=0.00, max_digits=14, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    movement_type = models.CharField(choices=MOVEMENT_CHOICES, max_length=4, default='INC')

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.movement_type == 'INC':
                self.account.total += Decimal(self.amount)
            elif self.movement_type == 'EXP':
                self.account.total -= Decimal(self.amount)
            self.account.save()

        super(Movement, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.account.name} | {self.movement_type} - {self.amount}"


class Transfer(BaseModel):
    from_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='from_transfers')
    to_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='to_transfers')
    amount = models.DecimalField(default=0.00, max_digits=14, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.from_account.total -= Decimal(self.amount)
            self.to_account.total += Decimal(self.amount)
            self.from_account.save()
            self.to_account.save()

        super(Transfer, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.from_account.name} -> {self.to_account.name}  ({self.amount})"


class Debt(BaseModel):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    due_date = models.DateField(default=timezone.now)
    amount = models.DecimalField(default=0.00, max_digits=14, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.amount}"
