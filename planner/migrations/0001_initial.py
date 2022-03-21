# Generated by Django 4.0.3 on 2022-03-06 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140, verbose_name='Name')),
                ('link', models.CharField(max_length=120, unique=True, verbose_name='Link')),
                ('image_link', models.CharField(max_length=300, unique=True, verbose_name='Image_Link')),
                ('type', models.CharField(choices=[('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('COFFEE', 'Coffee'), ('SOUP', 'Soup'), ('DINNER', 'Dinner')], max_length=20)),
                ('cooktime', models.IntegerField()),
                ('number_of_incredients', models.IntegerField()),
                ('preparation', models.TextField()),
                ('incredientstext', models.CharField(max_length=500, verbose_name='Incredients Text')),
                ('incredients', models.ManyToManyField(to='planner.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe_Ingredient_Mapping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('quantity', models.FloatField()),
                ('measure', models.CharField(choices=[('CM', 'cm'), ('WF', 'Wf'), ('G', 'g'), ('SCHB', 'Schb'), ('EL', 'EL'), ('MSP', 'Msp'), ('BECHER', 'Becher'), ('TASSE', 'Tasse'), ('KN', 'Kn'), ('ML', 'ml'), ('KPF', 'kpf'), ('BUND', 'Bund'), ('PA', 'Pa'), ('ZWEIG', 'Zweig'), ('PK', 'Pk'), ('SPR', 'Spr'), ('KG', 'kg'), ('SCHUSS', 'Schuss'), ('DOSE', 'Dose'), ('CL', 'cl'), ('SP', 'Sp'), ('STK', 'Stk'), ('TL', 'TL'), ('L', 'l'), ('TR', 'Tr'), ('MG', 'mg'), ('STG', 'Stg'), ('PRISE', 'Prise'), ('KUGEL', 'Kugel'), ('BL', 'Bl')], max_length=20)),
                ('created_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('incredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incredient', to='planner.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='planner.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Mealplan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('day_number', models.IntegerField()),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('created_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mealplan_recipe', to='planner.recipe')),
            ],
        ),
    ]
