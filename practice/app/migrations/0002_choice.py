# Generated by Django 2.1.7 on 2019-07-04 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Hello')),
            ],
        ),
    ]