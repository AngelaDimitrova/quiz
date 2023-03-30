# Generated by Django 4.0.5 on 2022-06-17 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labDj', '0014_remove_usermodel_skills_skills_skill_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=30)),
                ('interest_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='labDj.usermodel')),
            ],
        ),
    ]
