# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-26 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=60)),
                ('enabled', models.BooleanField()),
                ('checkitem', models.BooleanField()),
            ],
            options={
                'db_table': 'attributelist',
            },
        ),
        migrations.CreateModel(
            name='Nas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vhost', models.CharField(help_text='NAS Name (or IP address)', max_length=128, unique=True)),
                ('nasname', models.CharField(help_text='NAS Name (or IP address)', max_length=128, unique=True)),
                ('shortname', models.CharField(max_length=32)),
                ('type', models.CharField(choices=[('cisco', 'cisco'), ('computone', 'computone'), ('livingston', 'livingston'), ('max40xx', 'max40xx'), ('multitech', 'multitech'), ('netserver', 'netserver'), ('pathras', 'pathras'), ('patton', 'patton'), ('portslave', 'portslave'), ('tc', 'tc'), ('usrhiper', 'usrhiper'), ('other', 'other')], max_length=30)),
                ('secret', models.CharField(help_text='Shared Secret', max_length=60)),
                ('coasecret', models.CharField(blank=True, help_text='CoA Secret', max_length=60, null=True)),
                ('ports', models.IntegerField(blank=True, null=True)),
                ('naslocation', models.CharField(blank=True, max_length=32, null=True)),
                ('community', models.CharField(blank=True, max_length=50, null=True)),
                ('snmp', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'nas',
                'verbose_name_plural': 'nas',
            },
        ),
        migrations.CreateModel(
            name='Radacct',
            fields=[
                ('radacctid', models.AutoField(primary_key=True, serialize=False)),
                ('acctsessionid', models.CharField(max_length=32)),
                ('acctuniqueid', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=253, null=True)),
                ('realm', models.CharField(max_length=64, null=True)),
                ('nasipaddress', models.GenericIPAddressField()),
                ('nasportid', models.CharField(max_length=15, null=True)),
                ('nasporttype', models.CharField(max_length=32, null=True)),
                ('acctstarttime', models.DateTimeField(null=True)),
                ('acctstoptime', models.DateTimeField(null=True)),
                ('acctsessiontime', models.BigIntegerField(null=True)),
                ('acctauthentic', models.CharField(max_length=32, null=True)),
                ('acctinputoctets', models.BigIntegerField(null=True)),
                ('acctoutputoctets', models.BigIntegerField(null=True)),
                ('calledstationid', models.CharField(max_length=50, null=True)),
                ('callingstationid', models.CharField(max_length=50, null=True)),
                ('framedipaddress', models.GenericIPAddressField(null=True)),
                ('connectinfo_start', models.CharField(max_length=50, null=True)),
                ('connectinfo_stop', models.CharField(max_length=50, null=True)),
                ('acctterminatecause', models.CharField(max_length=32, null=True)),
                ('servicetype', models.CharField(max_length=32, null=True)),
                ('framedprotocol', models.CharField(max_length=32, null=True)),
                ('acctstartdelay', models.IntegerField(null=True)),
                ('acctstopdelay', models.IntegerField(null=True)),
                ('xascendsessionsvrkey', models.CharField(max_length=10, null=True)),
            ],
            options={
                'db_table': 'radacct',
                'verbose_name_plural': 'radacct',
            },
        ),
        migrations.CreateModel(
            name='Radcheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('attribute', models.CharField(max_length=64)),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('==', '=='), ('+=', '+='), ('!=', '!='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<='), ('=~', '=~'), ('!~', '!~'), ('=*', '=*'), ('!*', '!*')], max_length=2)),
                ('value', models.CharField(max_length=253)),
            ],
            options={
                'db_table': 'radcheck',
                'verbose_name_plural': 'radcheck',
            },
        ),
        migrations.CreateModel(
            name='Radgroupcheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=64)),
                ('attribute', models.CharField(max_length=64)),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('==', '=='), ('+=', '+='), ('!=', '!='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<='), ('=~', '=~'), ('!~', '!~'), ('=*', '=*'), ('!*', '!*')], max_length=2)),
                ('value', models.CharField(max_length=253)),
            ],
            options={
                'db_table': 'radgroupcheck',
                'verbose_name_plural': 'radgroupcheck',
            },
        ),
        migrations.CreateModel(
            name='Radgroupreply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=64)),
                ('attribute', models.CharField(max_length=64)),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('+=', '+=')], max_length=2)),
                ('value', models.CharField(max_length=253)),
            ],
            options={
                'db_table': 'radgroupreply',
                'verbose_name_plural': 'radgroupreply',
            },
        ),
        migrations.CreateModel(
            name='Radippool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool_name', models.CharField(help_text='The IP Pool name', max_length=64)),
                ('framedipaddress', models.GenericIPAddressField(help_text='The users IP address')),
                ('nasipaddress', models.CharField(max_length=16)),
                ('callingstationid', models.TextField(help_text='The MAC Address or CLI of the user', verbose_name='Calling-Station-Id')),
                ('expiry_time', models.DateTimeField(help_text='The IP Lease expiry time')),
                ('username', models.CharField(max_length=64)),
                ('groupname', models.CharField(max_length=30)),
                ('pool_key', models.CharField(max_length=30)),
                ('fixed', models.BooleanField()),
            ],
            options={
                'db_table': 'radippool',
                'verbose_name_plural': 'radippool',
            },
        ),
        migrations.CreateModel(
            name='Radpostauth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(db_column='pass', max_length=64)),
                ('reply', models.CharField(max_length=32)),
                ('authdate', models.DateTimeField()),
                ('calledstationid', models.CharField(max_length=64)),
                ('callingstationid', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'radpostauth',
                'verbose_name_plural': 'radpostauth',
            },
        ),
        migrations.CreateModel(
            name='Radreply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('attribute', models.CharField(max_length=30)),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('+=', '+=')], max_length=2)),
                ('value', models.CharField(max_length=40)),
                ('calledstationid', models.CharField(max_length=64)),
                ('custid', models.IntegerField()),
            ],
            options={
                'db_table': 'radreply',
                'verbose_name_plural': 'radreply',
            },
        ),
        migrations.CreateModel(
            name='Radusergroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('groupname', models.CharField(max_length=30)),
                ('calledstationid', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'radusergroup',
            },
        ),
        migrations.CreateModel(
            name='Realmgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realmname', models.CharField(max_length=30)),
                ('groupname', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'realmgroup',
            },
        ),
        migrations.CreateModel(
            name='Realms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realmname', models.CharField(max_length=64)),
                ('nas', models.CharField(max_length=128)),
                ('authport', models.IntegerField()),
                ('options', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'realms',
                'verbose_name_plural': 'realms',
            },
        ),
    ]