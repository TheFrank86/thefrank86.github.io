from django.core.management.base import BaseCommand
import pandas as pd
from carddisplay.models import card

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        set = "s:m21"
        df1 = pd.read_csv(f"https://api.scryfall.com/cards/search?format=csv&q={set} ", usecols = ['set', 'name', 'image_uri'])
        for SET,NAME,IMAGE in zip(df1.set,df1.name,df1.image_uri):
            models=card(set=SET,name=NAME,image=IMAGE)
            models.save()