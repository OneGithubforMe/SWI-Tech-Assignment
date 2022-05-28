# Generated by Django 4.0.4 on 2022-05-28 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrugReview',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('condition', models.CharField(max_length=200)),
                ('date', models.FloatField()),
                ('drug_name', models.CharField(max_length=200)),
                ('rating', models.PositiveIntegerField()),
                ('review', models.TextField()),
                ('unique_id', models.PositiveIntegerField()),
                ('useful_count', models.PositiveIntegerField()),
            ],
        ),
    ]
