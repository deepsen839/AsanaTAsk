# Generated by Django 4.0.2 on 2022-02-11 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asanaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('task_id', models.IntegerField(null=True)),
            ],
        ),
    ]
