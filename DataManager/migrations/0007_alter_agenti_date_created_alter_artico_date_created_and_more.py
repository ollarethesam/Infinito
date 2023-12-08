# Generated by Django 4.2.5 on 2023-12-01 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataManager', '0006_alter_agenti_date_created_alter_artico_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenti',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='artico',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='aspest',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='banche',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='catcon',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='catego',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='conabi',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='destcl',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='eseiva',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='ivaven',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='modpag',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='nazion',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='piacon',
            name='codcon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DataManager.conabi'),
        ),
        migrations.AlterField(
            model_name='piacon',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='valute',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='date_created',
            field=models.DateTimeField(default='2023-12-01 15:49:53'),
        ),
    ]
