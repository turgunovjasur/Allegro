# Generated by Django 4.2.10 on 2024-03-04 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bolim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Xabarlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50, null=True)),
                ('shablon', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yangiliklar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yangilik', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shaxs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=10)),
                ('familiya', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('qoshilgan_vaqt', models.DateTimeField(auto_now_add=True)),
                ('bolim', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='allegro.bolim')),
            ],
        ),
        migrations.CreateModel(
            name='Ariza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.TextField(null=True)),
                ('shaxs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allegro.shaxs')),
                ('xabar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xabarlar', to='allegro.xabarlar')),
            ],
        ),
    ]
