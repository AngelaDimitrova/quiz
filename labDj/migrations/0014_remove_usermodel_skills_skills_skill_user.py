# Generated by Django 4.0.5 on 2022-06-17 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labDj', '0013_rename_skils_skills_usermodel_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='skills',
        ),
        migrations.AddField(
            model_name='skills',
            name='skill_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='labDj.usermodel'),
        ),
    ]