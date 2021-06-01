from django.contrib import admin
from .models import Produit
from.models import Emballage
from.models import Fournisseur
from.models import ProduitNC
from .models import Commande,Customer,Order



# Register your models here.
admin.site.register(Produit)
admin.site.register(Emballage)
admin.site.register(Fournisseur)
admin.site.register(ProduitNC)
admin.site.register(Commande)
admin.site.register(Customer)
admin.site.register(Order)


