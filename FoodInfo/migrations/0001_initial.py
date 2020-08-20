# Generated by Django 3.0.8 on 2020-08-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('index', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('serving_wt', models.FloatField(blank=True, null=True)),
                ('kcal', models.FloatField(blank=True, null=True)),
                ('carbo', models.TextField(blank=True, null=True)),
                ('protein', models.TextField(blank=True, null=True)),
                ('fat', models.TextField(blank=True, null=True)),
                ('company', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Table',
                'managed': False,
            },
        ),
    ]
