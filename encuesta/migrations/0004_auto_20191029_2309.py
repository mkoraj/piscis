# Generated by Django 2.2.5 on 2019-10-30 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0003_auto_20191029_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='image',
            field=models.ImageField(default='static/Scatter_Mh_vs_Ms.png', upload_to='encuesta'),
        ),
    ]
