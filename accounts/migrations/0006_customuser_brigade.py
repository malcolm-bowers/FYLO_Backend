# Generated by Django 4.1.7 on 2023-04-01 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_customuser'),
        ('accounts', '0005_customuser_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='brigade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='app.brigade'),
        ),
    ]
