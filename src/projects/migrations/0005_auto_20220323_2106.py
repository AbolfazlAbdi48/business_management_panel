# Generated by Django 3.2.5 on 2022-03-23 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20220319_1658'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ('-id',), 'verbose_name': 'صورتحساب', 'verbose_name_plural': 'صورتحساب ها'},
        ),
        migrations.AlterModelOptions(
            name='workday',
            options={'ordering': ('-date',), 'verbose_name': 'روز کاری', 'verbose_name_plural': 'روزهای کاری'},
        ),
        migrations.AddField(
            model_name='workday',
            name='description',
            field=models.CharField(default=1, max_length=75, verbose_name='توضیحات'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workday',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workdays', to='projects.project', verbose_name='پروژه'),
        ),
    ]