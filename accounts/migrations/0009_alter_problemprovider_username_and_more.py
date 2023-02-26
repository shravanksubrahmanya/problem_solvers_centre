# Generated by Django 4.1 on 2023-02-26 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_problemprovider_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemprovider',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ProblemProvider', to=settings.AUTH_USER_MODEL, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='problemsolver',
            name='address',
            field=models.CharField(blank=True, max_length=200, verbose_name='Address '),
        ),
        migrations.AlterField(
            model_name='problemsolver',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Firstname '),
        ),
        migrations.AlterField(
            model_name='problemsolver',
            name='id_card_number',
            field=models.CharField(blank=True, max_length=10, verbose_name='Personal identity card number '),
        ),
        migrations.AlterField(
            model_name='problemsolver',
            name='personal_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='problemsolver',
            name='ph_no',
            field=models.CharField(blank=True, max_length=10, verbose_name='Phone Number '),
        ),
        migrations.AlterField(
            model_name='problemsolver',
            name='pin_code',
            field=models.CharField(blank=True, max_length=6, verbose_name='Pin Code '),
        ),
        migrations.AlterField(
            model_name='problemsolver',
            name='username',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProblemSolver', to=settings.AUTH_USER_MODEL, verbose_name='username'),
        ),
    ]
