# Generated by Django 4.0.5 on 2022-11-24 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_product_model_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.product_model')),
                ('user', models.ForeignKey(default='N/A', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
