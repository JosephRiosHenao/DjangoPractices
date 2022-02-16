# Generated by Django 4.0.2 on 2022-02-15 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProductType',
            fields=[
                ('ID', models.AutoField(max_length=16, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TypeMovement',
            fields=[
                ('ID', models.AutoField(max_length=16, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('operator', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ServicesProduct',
            fields=[
                ('ID', models.AutoField(max_length=16, primary_key=True, serialize=False)),
                ('nameProdServ', models.CharField(max_length=200)),
                ('dateIn', models.DateField()),
                ('observation', models.CharField(max_length=200)),
                ('exists', models.IntegerField(max_length=12)),
                ('serviceProductTypeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Service.serviceproducttype')),
                ('stateID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.state')),
            ],
        ),
        migrations.CreateModel(
            name='MovProdServ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateMov', models.DateField()),
                ('observation', models.CharField(max_length=60)),
                ('ProdServID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prodServ', to='Service.servicesproduct')),
                ('TypeProdServID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='typeProdServ', to='Service.servicesproduct')),
                ('clientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='Client.client')),
                ('typeDocClientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='typeDocClient', to='Client.client')),
                ('typeMovementID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Service.typemovement')),
            ],
        ),
    ]