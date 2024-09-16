# Generated by Django 5.1 on 2024-09-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raise_Request_Documentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rqstnr', models.CharField(max_length=500, unique=True)),
                ('desc', models.CharField(blank=True, max_length=500, null=True)),
                ('rqstd_date', models.DateField(blank=True, null=True)),
                ('rqstd_date_time', models.DateTimeField(auto_now_add=True)),
                ('module', models.IntegerField(choices=[(1, 'Internal'), (2, 'External')], default=0)),
                ('approve_type', models.CharField(blank=True, max_length=10, null=True)),
                ('approve_by', models.CharField(blank=True, max_length=10, null=True)),
                ('hd_app_sts', models.IntegerField(default=7)),
                ('approve_sts', models.IntegerField(default=0)),
                ('approve_timestamp', models.DateTimeField(auto_now_add=True)),
                ('hd_app_date', models.DateTimeField(auto_now_add=True)),
                ('usr_sts', models.IntegerField(blank=True, default=1, null=True)),
                ('delete1', models.IntegerField(blank=True, default=0, null=True)),
                ('tag_confirm_type', models.CharField(blank=True, max_length=500, null=True)),
                ('attach_file_original', models.CharField(blank=True, max_length=500, null=True)),
                ('attach_file_rename', models.CharField(blank=True, max_length=500, null=True)),
                ('dept', models.CharField(blank=True, max_length=500, null=True)),
                ('reqt_type', models.IntegerField(choices=[(1, 'Error'), (2, 'Authorization'), (3, 'Additions/Improvement'), (4, 'New Report'), (5, 'New Project'), (6, 'Project New Version')], default=0)),
                ('rmrks', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
