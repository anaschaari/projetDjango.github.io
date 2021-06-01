from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Produit(models.Model):
    TYPE_CHOICES=[('fr','Frais'),('cs','Conserve'),('em','emballe')]
    name=models.CharField(max_length=100)
    description=models.TextField(default='Non definie')
    prix=models.DecimalField(max_digits=10,decimal_places=3)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True)
    emballage=models.OneToOneField('Emballage',on_delete=models.CASCADE,null=True)
    fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "libelle {} description {} prix {} type{}".format(self.name,self.description,self.prix,self.type)
class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)

    def __str__(self):
        return self.Duree_garantie
class Emballage(models.Model):
    TYPE_CHOICES=[('bl','blanc'),('rg','rouge'),('ble','bleur'),('vr','vert'),('muli','multicolore')]
    matiere=models.CharField(max_length=100)
    couleur=models.CharField(max_length=10,choices=TYPE_CHOICES,default='Transparent')
    def __str__(self):
        return "matiere {} couleur {}".format(self.matiere,self.couleur)
class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return "nom {} adresse {} email {} telephone {}".format(self.nom,self.adresse,self.email,self.telephone)
        _
class Commande(models.Model):
    Duree_garantie=models.CharField(max_length=100)
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    product = models.ForeignKey(Produit, null=True, on_delete= models.SET_NULL)
    def __str__(self):
        return "durre_garantie{} date de commande {} total Commandes {} produits{}".format(self.Duree_garantie,self.dateCde,self.totalCde,self.product)

class Customer(models.Model):
    user = models.OneToOneField(User, null=True,blank=True,  on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
	    return self.name


class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Produit, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return str(self.product)
