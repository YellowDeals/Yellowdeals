# Generated by Django 5.1.1 on 2025-04-23 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YellowDealsAPP', '0013_typecomplaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeowner',
            name='status',
            field=models.CharField(choices=[('pending', 'รอการตรวจสอบ'), ('need_info', 'รอข้อมูลเพิ่มเติม'), ('active', 'กำลังใช้งาน'), ('banned', 'ถูกแบน')], default='pending', max_length=20),
        ),
    ]
