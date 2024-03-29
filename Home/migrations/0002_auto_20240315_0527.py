# Generated by Django 3.2.12 on 2024-03-15 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=15)),
                ('color_used', models.TextField()),
                ('color_code', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='people',
            name='color_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colorsss', to='Home.colors'),
        ),
    ]
