# Generated by Django 3.2.6 on 2021-08-02 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=128, verbose_name='Ф.И.О.')),
                ('sex', models.IntegerField(choices=[(1, 'Мужской'), (2, 'Женский'), (3, 'Неопределенный')], verbose_name='Пол')),
                ('marital', models.IntegerField(choices=[(1, 'Замужем / Женат'), (2, 'Не замужем / Не женат'), (3, 'Раздельное проживание'), (4, 'Разведен(а)'), (5, 'Вдовец / Вдова')], verbose_name='Семейное Положение')),
                ('nationality', models.CharField(max_length=64, verbose_name='Национальность')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
