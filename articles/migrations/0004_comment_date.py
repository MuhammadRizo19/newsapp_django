# Generated by Django 4.1 on 2022-08-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_comment_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=15.0),
            preserve_default=False,
        ),
    ]
