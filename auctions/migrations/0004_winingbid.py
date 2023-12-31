# Generated by Django 4.2.8 on 2023-12-31 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_remove_listing_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='WiningBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wining_bid', to='auctions.bid')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wining_listing', to='auctions.listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wining_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
