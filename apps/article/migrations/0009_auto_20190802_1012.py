# Generated by Django 2.0.12 on 2019-08-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20190408_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
