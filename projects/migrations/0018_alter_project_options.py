# Generated by Django 4.0.3 on 2022-03-17 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_alter_project_vote_ratio_alter_project_vote_total'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]