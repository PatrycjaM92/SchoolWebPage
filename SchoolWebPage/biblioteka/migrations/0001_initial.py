# Generated by Django 4.1 on 2022-08-13 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutorKsiazki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=20)),
                ('nazwisko', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(blank=True, choices=[('fsci', 'fantasy,science-fiction'), ('h', 'horror'), ('k', 'kryminał'), ('lm', 'literatura młodzieżowa'), ('lo', 'literatura obyczajowa'), ('ph', 'powieść historyczna'), ('pp', 'powieść przygodowa'), ('pn', 'literatura popularno-naukowa'), ('b', 'bajki'), ('bl', 'baśnie,legendy'), ('ld', 'literatura dziecięca'), ('o', 'opowiadania'), ('w', 'wiersze')], default='pp', help_text='Kategoria', max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Biblioteka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=200)),
                ('opis', models.TextField(blank=True, null=True)),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='autor', to='biblioteka.autorksiazki')),
            ],
            options={
                'ordering': ['tytul'],
            },
        ),
    ]