# Generated by Django 3.2 on 2021-05-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plateform', '0015_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='edf',
            name='decision',
            field=models.CharField(choices=[('Epileptic', 'Epileptic'), ('No Epileptic', 'No Epileptic')], max_length=100, null=True),
        ),
    ]
