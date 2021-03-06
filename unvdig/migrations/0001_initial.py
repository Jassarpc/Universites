# Generated by Django 2.1.2 on 2018-10-21 06:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_limite', models.DateField(default=datetime.date.today)),
                ('annee', models.CharField(default='', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=255)),
                ('prenom', models.CharField(default='', max_length=255)),
                ('email', models.CharField(default='', max_length=255)),
                ('pays', models.CharField(default='', max_length=255)),
                ('passport', models.FileField(default=None, upload_to='')),
                ('photo', models.FileField(default=None, upload_to='')),
                ('transcripts', models.FileField(default=None, upload_to='')),
                ('diplomes', models.FileField(default=None, upload_to='')),
                ('recommandations', models.FileField(default=None, upload_to='')),
                ('admission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unvdig.Admission')),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=255)),
                ('prenom', models.CharField(default='', max_length=255)),
                ('avatar', models.FileField(default=None, upload_to='')),
                ('email', models.CharField(default='', max_length=255)),
                ('sexe', models.CharField(choices=[('MASCULIN', 'Femminin'), ('FEMMININ', 'Masculin')], default='MASCULIN', max_length=8)),
                ('date_inscription', models.DateField(default=datetime.date.today)),
                ('username', models.CharField(default='', max_length=255)),
                ('password', models.CharField(default='', max_length=255)),
                ('code_enseignant', models.CharField(default=0, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=255)),
                ('prenom', models.CharField(default='', max_length=255)),
                ('avatar', models.FileField(default=None, upload_to='')),
                ('email', models.CharField(default='', max_length=255)),
                ('sexe', models.CharField(choices=[('MASCULIN', 'Femminin'), ('FEMMININ', 'Masculin')], default='MASCULIN', max_length=8)),
                ('date_inscription', models.DateField(default=datetime.date.today)),
                ('username', models.CharField(default='', max_length=255)),
                ('password', models.CharField(default='', max_length=255)),
                ('date_naissance', models.DateField(default=datetime.date.today)),
                ('lieu_naissance', models.CharField(default='', max_length=255)),
                ('pays', models.CharField(default='Vietnam', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(default='', max_length=255)),
                ('credit', models.CharField(default='4', max_length=2)),
                ('enseignant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unvdig.Enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(default='1', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etudiant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unvdig.Etudiant')),
                ('matiere_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unvdig.Matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Parcours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unvdig.Cycle')),
                ('niveau_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unvdig.Niveau')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.CharField(default='2018-2019', max_length=255)),
                ('numero', models.CharField(default=22, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=255)),
                ('prenom', models.CharField(default='', max_length=255)),
                ('avatar', models.FileField(default=None, upload_to='')),
                ('email', models.CharField(default='', max_length=255)),
                ('sexe', models.CharField(choices=[('MASCULIN', 'Femminin'), ('FEMMININ', 'Masculin')], default='MASCULIN', max_length=8)),
                ('date_inscription', models.DateField(default=datetime.date.today)),
                ('username', models.CharField(default='', max_length=255)),
                ('password', models.CharField(default='', max_length=255)),
                ('code_responsable', models.CharField(default=0, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='parcours',
            name='responsable_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unvdig.Responsable'),
        ),
        migrations.AddField(
            model_name='matiere',
            name='parcours_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unvdig.Parcours'),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='promotion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unvdig.Promotion'),
        ),
        migrations.AddField(
            model_name='admission',
            name='parcours_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unvdig.Parcours'),
        ),
    ]
