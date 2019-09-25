# Generated by Django 2.2.5 on 2019-09-25 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=10)),
                ('subtitle', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=10)),
                ('isbn', models.CharField(max_length=13)),
            ],
        ),
    ]
