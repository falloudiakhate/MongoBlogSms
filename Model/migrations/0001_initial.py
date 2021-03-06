# Generated by Django 2.2.11 on 2020-03-14 11:56

import Model.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sms', models.DateTimeField(default=django.utils.timezone.now)),
                ('image_sms', models.ImageField(blank=True, null=True, upload_to='')),
                ('contenu_sms', models.CharField(max_length=500)),
                ('author_sms_username', models.CharField(max_length=50)),
                ('recepteur_sms_username', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_data_publication', djongo.models.fields.EmbeddedField(model_container=Model.models.MetaDataPublication, null=True)),
                ('author_pub_username', models.CharField(blank=True, max_length=50, null=True)),
                ('photo_pub', models.ImageField(upload_to='')),
                ('commentaire', djongo.models.fields.EmbeddedField(model_container=Model.models.Commentaire, null=True)),
                ('tag', djongo.models.fields.EmbeddedField(model_container=Model.models.Tag, null=True)),
                ('categorie', djongo.models.fields.EmbeddedField(model_container=Model.models.Categorie, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_statut', models.DateTimeField(default=django.utils.timezone.now)),
                ('image_statut', models.ImageField(blank=True, null=True, upload_to='')),
                ('contenu_statut', models.CharField(max_length=100)),
                ('author_statut_username', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='')),
                ('promo', models.CharField(max_length=50)),
                ('genie', models.CharField(max_length=50)),
                ('entreprise_actuelle', models.CharField(blank=True, default='Aucun', max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
