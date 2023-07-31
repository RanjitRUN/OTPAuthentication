# Generated by Django 4.2.3 on 2023-07-27 07:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('OTPAuthApp', '0002_profile_created_at_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default=uuid.uuid4, max_length=200, unique=True),
        ),
    ]
