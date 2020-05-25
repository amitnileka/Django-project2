import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','gainsome.settings')


import django
django.setup()


import random
from gogo.models import AcsessRecord,Topic,webpage
from faker import Faker


fakegen=Faker()

topics=['social','market','news','games','history']
def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):


        #get the topuc for the entry
        top=add_topic()
        #Create the fake data for entry

        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        #create thw new webpage entry
        webpg=webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create fake accesrecord
        acc_rec=AcsessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=='__main__':
    print("populating script")
    populate(20)
    print("populating complte")
