# Generated by Django 4.0.3 on 2022-05-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_avatar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
