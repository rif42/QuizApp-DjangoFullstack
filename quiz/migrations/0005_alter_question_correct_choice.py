# Generated by Django 4.1.3 on 2023-12-30 10:24

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_delete_questionchoice_question_correct_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_choice',
            field=models.ForeignKey(default=1, limit_choices_to={'question': django.db.models.expressions.OuterRef('pk')}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='quiz.choice'),
        ),
    ]
