# Generated by Django 4.2.5 on 2023-11-30 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DataManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conabi',
            fields=[
                ('codcon', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('descon', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(default='2023-11-30 15:29:49')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'db_table': 'conabi',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='agenti',
            name='date_created',
            field=models.DateTimeField(default='2023-11-30 15:29:49'),
        ),
        migrations.AlterField(
            model_name='artico',
            name='date_created',
            field=models.DateTimeField(default='2023-11-30 15:29:49'),
        ),
        migrations.AlterField(
            model_name='aspest',
            name='date_created',
            field=models.DateTimeField(default='2023-11-30 15:29:49'),
        ),
        migrations.AlterField(
            model_name='banche',
            name='date_created',
            field=models.DateTimeField(default='2023-11-30 15:29:49'),
        ),
        migrations.AlterField(
            model_name='catego',
            name='date_created',
            field=models.DateTimeField(default='2023-11-30 15:29:49'),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_created',
            field=models.DateTimeField(default='2023-11-30 15:29:49'),
        ),
        migrations.AlterField(
            model_name='destcl',
            name='date_created',
            field=models.DateTimeField(default='2023-11-30 15:29:49'),
        ),
        migrations.AlterField(
            model_name='eseiva',
            name='date_created',
            field=models.DateTimeField(default='2023-11-30 15:29:49'),
        ),
        migrations.AlterField(
            model_name='ivaven',
            name='date_created',
            field=models.DateTimeField(default='2023-11-30 15:29:49'),
        ),
        migrations.AlterField(
            model_name='modpag',
            name='date_created',
            field=models.DateTimeField(default='2023-11-30 15:29:49'),
        ),
        migrations.AlterField(
            model_name='nazion',
            name='date_created',
            field=models.DateTimeField(default='2023-11-30 15:29:49'),
        ),
        migrations.AlterField(
            model_name='valute',
            name='date_created',
            field=models.DateTimeField(default='2023-11-30 15:29:49'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='date_created',
            field=models.DateTimeField(default='2023-11-30 15:29:49'),
        ),
        migrations.CreateModel(
            name='Piacon',
            fields=[
                ('codpia', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('despia', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(default='2023-11-30 15:29:49')),
                ('codcon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataManager.conabi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'db_table': 'piacon',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Catcon',
            fields=[
                ('codcat', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('descat', models.CharField(max_length=50, unique=True)),
                ('date_created', models.DateTimeField(default='2023-11-30 15:29:49')),
                ('codpia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataManager.piacon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'db_table': 'catcon',
                'managed': True,
            },
        ),
    ]
