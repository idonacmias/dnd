# Generated by Django 4.1.4 on 2022-12-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cretures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cretures',
            name='Charisma',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cretures',
            name='Constitution',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cretures',
            name='Dexterity',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cretures',
            name='Intelligence',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cretures',
            name='Strength',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cretures',
            name='Wisdom',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cretures',
            name='proficiency',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
