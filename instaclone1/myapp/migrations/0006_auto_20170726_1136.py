# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 06:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20170724_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=555)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostLikeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='PostModel',
        ),
        migrations.RemoveField(
            model_name='sessiontoken',
            name='last_request_on',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='has_verified_mobile',
        ),
        migrations.AlterField(
            model_name='sessiontoken',
            name='session_token',
            field=models.CharField(max_length=240),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(default=0, max_length=254),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(default=0, max_length=120),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(default=0, max_length=40),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(default=0, max_length=120),
        ),
        migrations.AddField(
            model_name='postlikemodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.PostModel'),
        ),
        migrations.AddField(
            model_name='postlikemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.UserModel'),
        ),
        migrations.AddField(
            model_name='postcommentmodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.PostModel'),
        ),
        migrations.AddField(
            model_name='postcommentmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.UserModel'),
        ),
    ]