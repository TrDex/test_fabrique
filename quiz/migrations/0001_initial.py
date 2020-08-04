# Generated by Django 2.2.10 on 2020-07-31 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Ответ на вопрос')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('type', models.CharField(max_length=256, unique=True, verbose_name='Тип вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('start_date', models.DateTimeField(verbose_name='Дата старта')),
                ('finish_date', models.DateTimeField(verbose_name='Дата окончания')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Ответ текстом', 'Ответ текстом'), ('Ответ с выбором одного варианта', 'Ответ с выбором одного варианта'), ('Ответ с выбором нескольких вариантов', 'Ответ с выбором нескольких вариантов')], max_length=256, verbose_name='Ответ на вопрос')),
                ('question_selected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question', verbose_name='Ответ с выбором')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz', verbose_name='Опрос'),
        ),
        migrations.CreateModel(
            name='AnswerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Answer', verbose_name='Ответ на вопрос')),
                ('answer_selected', models.ManyToManyField(to='quiz.QuestionItem', verbose_name='Ответы/Ответ на вопрос выбранные из списка ответов')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question', verbose_name='Вопрос'),
        ),
    ]
