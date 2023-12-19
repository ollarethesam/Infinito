# Generated by Django 4.2.5 on 2023-12-18 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataManager', '0027_alter_agenti_date_created_alter_artico_date_created_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='liscli',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='agenti',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='artico',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='aspest',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='banche',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='catcon',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='catego',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='cautra',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='cenlav',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='conabi',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='degrar',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='destcl',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='destfo',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='dipend',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='eseiva',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='fornit',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='ivaacq',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='ivacor',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='ivaven',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='liscli',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='modpag',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='nazion',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='piacon',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='porto',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='raggfi',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='spediz',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='tipall',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='valute',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AlterField(
            model_name='zone',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 18, 15, 38, 25), editable=False),
        ),
        migrations.AddConstraint(
            model_name='liscli',
            constraint=models.UniqueConstraint(fields=('codart', 'codcli'), name='liscli_sk'),
        ),
    ]
