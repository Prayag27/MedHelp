# Generated by Django 3.0.4 on 2020-05-24 08:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalDetails',
            fields=[
                ('dId', models.TextField(blank=True, max_length=200)),
                ('ResourceToQuant', models.TextField()),
                ('hospitalId', models.IntegerField(primary_key=True, serialize=False)),
                ('lat', models.IntegerField(default=0)),
                ('long', models.IntegerField(default=0)),
                ('pId', models.CharField(default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('lat', models.IntegerField()),
                ('long', models.IntegerField()),
                ('illnesses', multiselectfield.db.fields.MultiSelectField(choices=[('I1', 'Measles'), ('I2', 'Typhoid'), ('I3', 'Malaria'), ('I4', 'Flu')], default=None, max_length=11)),
                ('currentPrescriptions', models.TextField()),
                ('isAdmitted', models.BooleanField(default=None)),
                ('pId', models.IntegerField(primary_key=True, serialize=False)),
                ('hId', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration.HospitalDetails')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorDetails',
            fields=[
                ('dId', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('visStart', models.TimeField(default=django.utils.timezone.now)),
                ('visEnd', models.TimeField(default=django.utils.timezone.now)),
                ('lat', models.IntegerField(default=0)),
                ('long', models.IntegerField(default=0)),
                ('hospShiftStart', models.TimeField(default=django.utils.timezone.now)),
                ('hospShiftEnd', models.TimeField(default=django.utils.timezone.now)),
                ('patientId', models.CharField(max_length=100)),
                ('hId', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Registration.HospitalDetails')),
            ],
        ),
    ]
