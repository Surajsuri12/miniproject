# Generated by Django 4.0.3 on 2022-06-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='liked',
            name='username',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]