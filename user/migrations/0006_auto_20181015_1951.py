# Generated by Django 2.1.2 on 2018-10-15 19:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20181015_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performance',
            old_name='bassepay',
            new_name='basepay',
        ),
        migrations.RemoveField(
            model_name='position',
            name='role',
        ),
        migrations.AddField(
            model_name='vacation',
            name='busyday',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='事假'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='endday',
            field=models.DateField(default=datetime.datetime(2018, 10, 15, 19, 51, 14, 548024), verbose_name='请假结束日期'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startday',
            field=models.DateField(default=datetime.datetime(2018, 10, 15, 19, 51, 14, 548024), verbose_name='请假起始日期'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='发送人ID'),
        ),
        migrations.AlterField(
            model_name='out',
            name='endday',
            field=models.DateField(default=datetime.datetime(2018, 10, 15, 19, 51, 14, 548024), verbose_name='外出结束日期'),
        ),
        migrations.AlterField(
            model_name='out',
            name='startday',
            field=models.DateField(default=datetime.datetime(2018, 10, 15, 19, 51, 14, 548024), verbose_name='外出起始日期'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='salaryMonth',
            field=models.DateField(default=datetime.datetime(2018, 10, 15, 19, 51, 14, 548024), verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='section',
            name='section_remarks',
            field=models.TextField(null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='birth',
            field=models.DateField(default=datetime.datetime(2018, 10, 15, 19, 51, 14, 548024), verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='hiredate',
            field=models.DateField(default=datetime.datetime(2018, 10, 15, 19, 51, 14, 548024), verbose_name='入职日期'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_remarks',
            field=models.TextField(null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='illday',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='病假'),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='yearday',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='年假'),
        ),
    ]
