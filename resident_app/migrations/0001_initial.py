# Generated by Django 4.2.3 on 2023-07-18 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resident_name', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=255)),
                ('email_id', models.EmailField(max_length=254)),
                ('resident_building_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('rent_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('token_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contract_start_date', models.DateField()),
                ('contract_end_date', models.DateField()),
                ('move_in_date', models.DateField()),
                ('move_out_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
