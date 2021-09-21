# Generated by Django 3.2.7 on 2021-09-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cold_chambers', '0002_auto_20210916_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='coldchambers',
            name='photo',
            field=models.ImageField(default=10, help_text='Imagen que se mostrará en la pagina web', upload_to='camaras/', verbose_name='Imagen de camara de frio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coldchambers',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre de Camara'),
        ),
    ]