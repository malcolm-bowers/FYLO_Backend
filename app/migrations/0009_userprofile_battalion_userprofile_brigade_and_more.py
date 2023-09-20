# Generated by Django 4.1.7 on 2023-03-28 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_userprofile_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='battalion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.battalion'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='brigade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.brigade'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='command',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.command'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.company'),
        ),
    ]