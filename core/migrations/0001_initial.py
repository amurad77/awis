# Generated by Django 4.1.3 on 2022-11-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Involved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Ad')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('number', models.CharField(max_length=20, verbose_name='Telefon nömrəsi')),
                ('membership_type', models.CharField(choices=[('1', 'Select the role *'), ('2', 'Volunteer'), ('3', 'Partner'), ('4', 'Mentor'), ('5', 'Donor')], default='Select the role *', max_length=256, verbose_name='Membership type')),
                ('message', models.TextField(max_length=5000, verbose_name='Mesaj')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statitics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projects', models.IntegerField(default=0, verbose_name='local and international')),
                ('EUR', models.IntegerField(default=0, verbose_name='funds raised')),
                ('females', models.IntegerField(default=0, verbose_name='AWiS volunteers')),
                ('girls_mentees', models.IntegerField(default=0, verbose_name='AWiS mentees')),
                ('girls_regional', models.IntegerField(default=0, verbose_name='regional ambassadors')),
                ('followers', models.IntegerField(default=0, verbose_name='social media followers')),
                ('women', models.IntegerField(default=0, verbose_name='experts in network')),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Email')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
