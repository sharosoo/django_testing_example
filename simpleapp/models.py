import uuid as uuid_lib

from django.db import models
from django.urls import reverse


class Simple(models.Model):
    title = models.CharField(
        max_length=255
    )
    slug = models.SlugField(
        unique=True
    )
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4(),
        editable=False
    )
    point = models.IntegerField(
        default=0
    )

    def get_absolute_url(self):
        return reverse('simpleapp:detail', kwargs={'slug': self.slug})


