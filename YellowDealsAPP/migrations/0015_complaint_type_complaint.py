# Generated by Django 5.1.1 on 2025-04-23 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YellowDealsAPP', '0014_alter_storeowner_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='type_complaint',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='YellowDealsAPP.typecomplaint'),
        ),
    ]
