# Generated by Django 2.2.10 on 2020-07-31 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200731_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('answer_text', 'Ответ текстом'), ('answer_one_selected', 'Ответ с выбором одного варианта'), ('answer_some_selected', 'Ответ с выбором нескольких вариантов')], max_length=256, verbose_name='Тип вопроса'),
        ),
    ]