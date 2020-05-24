# Generated by Django 3.0.4 on 2020-05-24 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdNum', models.IntegerField(default=None)),
            ],
        ),
        migrations.AlterField(
            model_name='doctordetails',
            name='hId',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration.HospitalDetails'),
        ),
    ]