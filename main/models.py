from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from slugify import slugify


class BaseModel(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Seller(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def num_ads(self):
        actual_ads = list(self.ads.filter(archived=False))
        archived_ads = list(self.ads.filter(archived=True))
        ads_dict = {}
        ads_dict["actual"] = actual_ads
        ads_dict["archived"] = archived_ads
        return ads_dict

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"


class Category(BaseModel):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        allow_unicode=True
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


class Tag(BaseModel):
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


class Ad(BaseModel):
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
    tags = models.ManyToManyField('Tag', blank=True)
    price = models.PositiveIntegerField(
        default=0,
        blank=True,
        null=True
    )
    archived = models.BooleanField(default=False)
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

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def get_absolute_url(self):
        return reverse('ads-detail', kwargs={'pk': self.pk})


class ArchiveAdManager(models.Manager):
    def get_queryset(self):
        return Ad.objects.filter(archived=True)


class ArchiveAd(Ad):
    objects = ArchiveAdManager()

    class Meta:
        proxy = True


