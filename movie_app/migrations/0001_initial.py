# Generated by Django 3.1.2 on 2020-10-19 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mName', models.CharField(max_length=50)),
                ('mRdate', models.DateField()),
                ('mLang', models.CharField(max_length=80)),
            ],
        ),
    ]