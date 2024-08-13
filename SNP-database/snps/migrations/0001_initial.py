# Generated by Django 4.2.11 on 2024-06-26 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sampling_date', models.DateField()),
                ('sequencing_date', models.DateField()),
                ('specimen', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_genome', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='SNP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chromosome', models.IntegerField()),
                ('coordinate', models.IntegerField()),
                ('reference_allele', models.CharField(choices=[('A', 'A'), ('C', 'C'), ('T', 'T'), ('G', 'G')], max_length=1)),
                ('alternative_allele', models.CharField(choices=[('A', 'A'), ('C', 'C'), ('T', 'T'), ('G', 'G')], max_length=1)),
                ('MAF', models.FloatField()),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snps.sample')),
            ],
        ),
        migrations.AddField(
            model_name='sample',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='snps.species'),
        ),
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=10000)),
                ('SNP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snps.snp')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='snp',
            constraint=models.CheckConstraint(check=models.Q(('alternative_allele', models.F('reference_allele')), _negated=True), name='snips_cannot_be_equal'),
        ),
        migrations.AddConstraint(
            model_name='snp',
            constraint=models.CheckConstraint(check=models.Q(('MAF__gte', 0.0), ('MAF__lte', 0.5)), name='MAF_range'),
        ),
        migrations.AlterUniqueTogether(
            name='snp',
            unique_together={('chromosome', 'coordinate')},
        ),
        migrations.AddConstraint(
            model_name='sample',
            constraint=models.CheckConstraint(check=models.Q(('sequencing_date__gte', models.F('sampling_date'))), name='sequencing_later_than_sampling'),
        ),
        migrations.AlterUniqueTogether(
            name='sample',
            unique_together={('sampling_date', 'specimen', 'species')},
        ),
    ]