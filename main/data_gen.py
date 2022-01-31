from django.contrib.auth.models import User
from main.models import Seller, Ad, ArchiveAd, Tag, Category
import random
import string

# print(random.choices(string.ascii_lowercase))

list_of_tags = ['скидка', 'доставка', 'бесплатно', 'эко', 'первый', 'халяль', 'кошерно']
list_of_categories = ['Авто', 'Еда', 'Игрушки', 'Собутыльники']
if Seller.objects.count() == 0:
    seller_user = Seller.objects.create(user = User.objects.first())

Tag.objects.all().delete()
Category.objects.all().delete()

for i in list_of_tags:
    Tag.objects.create(name=i)

for i in list_of_categories:
    Category.objects.create(name=i)

for i in Category.objects.all():
    print(i.__dict__)


for i in range(1, 20):
    desc = ''.join(random.choices(string.ascii_lowercase, k=35))

    Ad.objects.create(
        name=desc[:4],
        description=desc,
        category=Category.objects.first(),
        seller=Seller.objects.first(),
        price=random.randint(1000, 10000)/100,
    )