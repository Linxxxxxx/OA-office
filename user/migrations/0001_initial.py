# Generated by Django 2.1.2 on 2018-10-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
