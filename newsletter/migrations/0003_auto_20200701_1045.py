# Generated by Django 3.0.7 on 2020-07-01 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_newsletter_newslettertemplate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='email',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='from_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='is_html',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='is_plaintxt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='to_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
