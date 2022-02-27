from django.contrib.auth.models import User
from main.models import Seller, Ad, ArchiveAd, Tag, Category
from pprint import pprint
import random
import string

def user_gen():
    User.objects.create_user(username='nurs', email='nurs@example.com', password='string')
    User.objects.create_user(username='turlan', email='turlan@example.com', password='string')
    User.objects.create_user(username='ilya', email='ilya@example.com', password='string')

def user_purge():
    for user in User.objects.filter(is_superuser=False):
        user.delete()

def seller_gen():
    for user in User.objects.all():
        Seller.objects.create(user=user)

def tag_gen():
    # list_of_tags = ['скидка', 'доставка', 'бесплатно', 'эко', 'первый', 'халяль', 'кошерно']
    for i in range(1, 40):
        Tag.objects.create(name=''.join(random.choices(string.ascii_lowercase, k=6)))

def category_gen():
    list_of_categories = ['Авто', 'Еда', 'Игрушки', 'Собутыльники']
    for i in list_of_categories:
        Category.objects.create(name=i)

def ad_gen():
    for x in Seller.objects.all():
        for y in Category.objects.all():
            for z in range(1,10):
                desc = ''.join(random.choices(string.ascii_lowercase, k=35))
                tags = random.sample(list(Tag.objects.all()), 4)

                ad = Ad.objects.create(
                    name=desc[:4],
                    description=desc,
                    category=y,
                    seller=x,
                    price=random.randint(10, 100),
                )
                for i in tags:
                    ad.tags.add(i)

                ad.save()

def purge(modelname):
    modelname.objects.all().delete()

def print_objects(modelname):
    print("---------------------")
    print(modelname)
    print("---------------------")
    for i in modelname.objects.all():
        print("******************")
        pprint(i.__dict__)

def archive_ad():
    ads = list(Ad.objects.all())
    for i in random.sample(ads, 10):
        i.archived = True
        i.save()

def print_sellers():
    for i in Seller.objects.all():
        pprint(i.user.username)
        pprint(i.num_ads)
        print('-----------------------')

def print_categories():
    for i in Category.objects.all():
        print('*************************')
        print(i.name)
        for j in Ad.objects.all():
            print(j.name)
            print('---------------------')


purge(Seller)
purge(Ad)
purge(Tag)
purge(Category)
user_purge()

user_gen()
seller_gen()
tag_gen()
category_gen()
ad_gen()
archive_ad()

for i in Seller.objects.all():
    pprint(i.avatar.url)
