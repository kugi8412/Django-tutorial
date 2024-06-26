# Generated by Django 4.2.11 on 2024-05-08 02:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='animal_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Chromosome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('start_position', models.IntegerField()),
                ('end_position', models.IntegerField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chromosomes', to='snps.animal')),
            ],
        ),
        migrations.CreateModel(
            name='SNP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('ref', models.CharField(choices=[('A', 'A'), ('C', 'C'), ('G', 'G'), ('T', 'T')], max_length=1)),
                ('alt', models.CharField(choices=[('A', 'A'), ('C', 'C'), ('G', 'G'), ('T', 'T')], max_length=1)),
                ('maf', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('chromosome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snps', to='snps.chromosome')),
            ],
        ),
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('snp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to='snps.snp')),
            ],
        ),
    ]
