# Generated by Django 3.1.6 on 2021-03-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_experience_overview1'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='title1',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]