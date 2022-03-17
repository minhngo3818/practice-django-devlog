# Generated by Django 4.0.3 on 2022-03-12 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_alter_review_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('up', 'Up Vote'), ('down', 'Down Vote')], max_length=200),
        ),
    ]