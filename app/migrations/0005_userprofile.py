# Generated by Django 4.1.7 on 2023-03-28 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.battalion')),
            ],
        ),
    ]