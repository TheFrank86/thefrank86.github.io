from django.core.management.base import BaseCommand
import pandas as pd
from carddisplay.models import card
# , search
# from views import *

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        #pass
        parser.add_argument('-s', '--sellect', type=str)

    def handle(self, *args, **kwargs):
        sellect = kwargs['sellect']
        #unique = "s:dmu"
        unique = f"s:{sellect}"
        df1 = pd.read_csv(f"https://api.scryfall.com/cards/search?format=csv&q={unique} ", usecols = ['set', 'name', 'image_uri'])
        for SET,NAME,IMAGE in zip(df1.set,df1.name,df1.image_uri):
            models=card(set=SET,name=NAME,image=IMAGE)
            models.save()