from django.contrib.auth.models import User
from main.models import Seller, Ad, ArchiveAd, Tag, Category

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
