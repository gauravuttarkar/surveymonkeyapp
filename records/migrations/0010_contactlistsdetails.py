# Generated by Django 2.0.5 on 2018-05-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0009_delete_contactlistsdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactListsDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_list_id', models.IntegerField()),
                ('contact_list_name', models.CharField(max_length=100)),
            ],
        ),
    ]
