# Generated by Django 4.1.3 on 2022-12-09 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('cname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('population', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseType',
            fields=[
                ('diseaseID', models.IntegerField(primary_key=True, serialize=False)),
                ('diseaseDescription', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=40)),
                ('salary', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test1.country')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Test1.users')),
                ('degree', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PublicServant',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Test1.users')),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disease_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pathogen', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=140)),
                ('diseaseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test1.diseasetype')),
            ],
        ),
        migrations.CreateModel(
            name='Discover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_enc_date', models.DateField()),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test1.country')),
                ('disease_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test1.disease')),
            ],
        ),
        migrations.CreateModel(
            name='Specialize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseaseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test1.diseasetype')),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Test1.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_deaths', models.IntegerField()),
                ('total_patients', models.IntegerField()),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test1.country')),
                ('disease_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test1.disease')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test1.publicservant')),
            ],
        ),
        migrations.AddConstraint(
            model_name='discover',
            constraint=models.UniqueConstraint(fields=('cname', 'disease_code'), name='Discover_constraint'),
        ),
        migrations.AddConstraint(
            model_name='specialize',
            constraint=models.UniqueConstraint(fields=('diseaseID', 'email'), name='specialize_constraint'),
        ),
        migrations.AddConstraint(
            model_name='record',
            constraint=models.UniqueConstraint(fields=('email', 'cname', 'disease_code'), name='record_constraint'),
        ),
    ]