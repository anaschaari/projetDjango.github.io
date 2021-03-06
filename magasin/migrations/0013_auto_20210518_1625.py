# Generated by Django 3.2 on 2021-05-18 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magasin', '0012_customer_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='produits',
        ),
        migrations.AddField(
            model_name='commande',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magasin.produit'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
