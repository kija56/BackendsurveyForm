# Generated by Django 4.1.3 on 2022-11-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_survey_remove_choice_question_delete_feedback_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='name',
            field=models.CharField(max_length=45, null=True),
        ),
    ]