# Generated by Django 3.2 on 2022-05-31 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
