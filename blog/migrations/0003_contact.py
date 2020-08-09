# Generated by Django 3.0.8 on 2020-08-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200806_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=12)),
                ('feedback', models.TextField()),
                ('time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
