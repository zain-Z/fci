# Generated by Django 3.2.3 on 2021-06-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0018_auto_20210602_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigntime',
            name='day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday')], max_length=15),
        ),
        migrations.AlterField(
            model_name='marks',
            name='name',
            field=models.CharField(choices=[('Quiz 1', 'Quiz 1'), ('Quiz 2', 'Quiz 2'), ('Quiz 3', 'Quiz 3'), ('MidTerm 1', 'MidTerm 1'), ('MidTerm 2', 'MidTerm 2'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='marksclass',
            name='name',
            field=models.CharField(choices=[('Quiz 1', 'Quiz 1'), ('Quiz 2', 'Quiz 2'), ('Quiz 3', 'Quiz 3'), ('MidTerm 1', 'MidTerm 1'), ('MidTerm 2', 'MidTerm 2'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
    ]