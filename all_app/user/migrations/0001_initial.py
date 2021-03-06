# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-25 09:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_deleted', models.BooleanField(default=False, editable=False, verbose_name='是否已删除')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='用户名')),
                ('password', models.CharField(blank=True, max_length=255, verbose_name='密码')),
                ('telephone', models.CharField(blank=True, max_length=255, unique=True, verbose_name='电话号码')),
                ('fullname', models.CharField(blank=True, max_length=255, verbose_name='姓名')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='加入时间')),
                ('session_id', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='是否激活')),
                ('is_admin', models.BooleanField(default=False, verbose_name='是否管理员')),
                ('is_online', models.IntegerField(default=0)),
                ('login_times', models.IntegerField(default=0)),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.File', verbose_name='用户头像')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'permissions': (('group_manage', '角色管理'), ('user_manage', '成员管理'), ('organization_manage', '组织管理')),
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_deleted', models.BooleanField(default=False, editable=False, verbose_name='是否已删除')),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('description', models.CharField(default='', max_length=255)),
                ('icon', models.CharField(default='', max_length=255)),
                ('order_num', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=1)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Menu')),
            ],
            options={
                'verbose_name': '菜单',
                'verbose_name_plural': '菜单',
            },
        ),
        migrations.CreateModel(
            name='OperationLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_deleted', models.BooleanField(default=False, editable=False, verbose_name='是否已删除')),
                ('detail', models.CharField(max_length=200, unique=True, verbose_name='操作详情')),
                ('operator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作人')),
            ],
            options={
                'verbose_name': '操作日志',
                'verbose_name_plural': '操作日志',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_deleted', models.BooleanField(default=False, editable=False, verbose_name='是否已删除')),
                ('name', models.CharField(max_length=32, verbose_name='组织名称')),
                ('organization_type', models.CharField(choices=[('公司', '公司'), ('部门', '部门')], max_length=32, verbose_name='组织类型')),
                ('parent_organization', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Organization', verbose_name='父组织')),
            ],
            options={
                'verbose_name': '组织',
                'verbose_name_plural': '组织',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_deleted', models.BooleanField(default=False, editable=False, verbose_name='是否已删除')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('menus', models.ManyToManyField(to='user.Menu')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organization_staffs', to='user.Organization', verbose_name='组织'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Role'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='organization',
            unique_together=set([('name', 'parent_organization')]),
        ),
    ]
