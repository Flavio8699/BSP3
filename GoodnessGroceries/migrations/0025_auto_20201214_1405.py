# Generated by Django 3.1.3 on 2020-12-14 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GoodnessGroceries', '0024_productreviews_static_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreviews',
            name='static_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='GoodnessGroceries.staticproducts'),
        ),
    ]
