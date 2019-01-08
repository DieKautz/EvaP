# Generated by Django 2.0.9 on 2018-10-29 19:48

from django.db import migrations


CONVERSION = {
    'T': 0,
    'L': 1,
    'G': 2,
    'P': 3,
    'N': 4,
    'H': 5
}


def question_types_convert_char_to_int(apps, _schema_editor):
    Question = apps.get_model('evaluation', 'Question')

    for char_type, int_type in CONVERSION.items():
        Question.objects.filter(type=char_type).update(int_type=int_type)


def question_types_convert_int_to_char(apps, _schema_editor):
    Question = apps.get_model('evaluation', 'Question')

    for char_type, int_type in CONVERSION.items():
        Question.objects.filter(int_type=int_type).update(type=char_type)


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0088_prepare_use_integers_and_groups_for_question_type'),
    ]

    operations = [
        migrations.RunPython(question_types_convert_char_to_int, question_types_convert_int_to_char),
        migrations.RemoveField(
            model_name='question',
            name='type'
        ),
        migrations.RenameField(
            model_name='question',
            old_name='int_type',
            new_name='type'
        )
    ]