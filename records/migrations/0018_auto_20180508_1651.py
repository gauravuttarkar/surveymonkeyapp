# Generated by Django 2.0.5 on 2018-05-08 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0017_contactlistsdetails_user_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contactlistsdetails',
            unique_together={('contact_list_id', 'contact_list_name')},
        ),
    ]
