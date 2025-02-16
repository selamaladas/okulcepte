# Generated by Django 5.0.3 on 2024-06-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msy_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ders',
            name='toplam_saat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='ders',
            name='status',
            field=models.CharField(blank=True, choices=[('mevcut', 'mevcut'), ('seçildi', 'seçildi'), ('tamamlandı', 'tamamlandı')], max_length=50, null=True),
        ),
    ]
