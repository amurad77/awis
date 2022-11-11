# Generated by Django 4.1.3 on 2022-11-11 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_eur_statitics_eur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/partners', verbose_name='Logo')),
            ],
        ),
        migrations.AlterField(
            model_name='involved',
            name='membership_type',
            field=models.CharField(choices=[('1', 'Select the role*'), ('2', 'Volunteer'), ('3', 'Partner'), ('4', 'Mentor'), ('5', 'Donor')], default='Select the role*', max_length=256, verbose_name='Membership type'),
        ),
    ]