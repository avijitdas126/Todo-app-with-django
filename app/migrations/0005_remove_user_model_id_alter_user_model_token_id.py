# Generated by Django 5.1.6 on 2025-02-22 18:08

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_todo_todo_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_model',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_model',
            name='token_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
