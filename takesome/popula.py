import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','takesome.settings')


import django
django.setup()

from faker import Faker
from give.models import jacob
fakegen=Faker()

def populate(N=10):
    for i in range(N):


        fake_nme=fakegen.name().split()
        fake_fnme=fake_nme[0]
        fake_lnme=fake_nme[1]
        fake_mail=fakegen.email()

        usre=jacob.objects.get_or_create(first_name=fake_fnme,last_name=fake_lnme,email=fake_mail)[0]


if __name__=='__main__':
    print("populating script")
    populate(20)
    print("populating complte")
