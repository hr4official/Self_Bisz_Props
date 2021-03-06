# Generated by Django 3.1.4 on 2021-03-23 08:15

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210323_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='registartion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=12)),
                ('confirm_password', models.CharField(max_length=12)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('o', 'other')], max_length=1)),
                ('phone_number', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
            ],
        ),
        migrations.DeleteModel(
            name='Reg',
        ),
    ]
