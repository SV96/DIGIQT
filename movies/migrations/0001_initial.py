# Generated by Django 2.2.12 on 2021-01-07 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scrapdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=10)),
                ('release_date', models.CharField(max_length=10)),
                ('duration', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
