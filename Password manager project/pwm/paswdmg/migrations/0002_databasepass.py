# Generated by Django 4.1.2 on 2022-10-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paswdmg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataBasePass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.TextField()),
                ('emailtosave', models.CharField(max_length=122)),
                ('passwordtosave', models.CharField(max_length=122)),
                ('name', models.CharField(max_length=122)),
            ],
        ),
    ]
