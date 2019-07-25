# Generated by Django 2.1.7 on 2019-06-10 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hope_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hope_app.Webpage')),
            ],
        ),
    ]
