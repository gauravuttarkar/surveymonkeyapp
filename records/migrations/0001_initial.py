# Generated by Django 2.0.5 on 2018-05-05 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yellowant_token', models.CharField(max_length=100)),
                ('yellowant_id', models.IntegerField(default=0)),
                ('yellowant_intergration_id', models.IntegerField(default=0)),
            ],
        ),
    ]
