# Generated by Django 3.2 on 2021-05-16 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0011_rename_libelle_produit_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
    ]
