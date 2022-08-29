# Generated by Django 4.1 on 2022-08-13 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_odpowiedz_pyt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zdjecia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='galeria')),
                ('tytul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wpis', to='blog.wpis')),
            ],
        ),
    ]
