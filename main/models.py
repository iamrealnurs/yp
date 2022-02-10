from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def ads_amount(self):
        return self.ads.count()

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )

    @property
    def ads_amount(self):
        return self.ads.count()

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class Ad(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    description = models.TextField(null=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='ads'
    )
    seller = models.ForeignKey(
        'Seller',
        on_delete=models.CASCADE,
        related_name='ads'
    )
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

