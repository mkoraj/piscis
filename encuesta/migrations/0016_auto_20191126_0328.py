# Generated by Django 2.2.5 on 2019-11-26 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0015_auto_20191126_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='imagen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuesta.Images'),
        ),
    ]
