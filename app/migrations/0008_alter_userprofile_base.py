# Generated by Django 4.1.7 on 2023-03-28 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='base',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.base'),
        ),
    ]