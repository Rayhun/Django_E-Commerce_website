from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=20)
    parent = TreeForeignKey(
        'self', 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True, 
        related_name='children',
        db_index=True,
        )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
