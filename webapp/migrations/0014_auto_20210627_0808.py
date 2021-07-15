# Generated by Django 2.1.14 on 2021-06-27 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insuree', '0004_confirmationtype_education_profession_relation'),
        ('webapp', '0013_auto_20210623_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, null=True)),
                ('photo', models.ImageField(upload_to='insuree/photo')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date added')),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date added')),
                ('insuree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webapp_insuree_profile', to='insuree.Insuree')),
            ],
        ),
        migrations.AlterField(
            model_name='voucherpayment',
            name='vocher_id',
            field=models.CharField(default='20210627080811', max_length=50),
        ),
    ]
