# Generated by Django 4.2.2 on 2023-06-20 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churras', '0003_prato_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='prato',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]
