# Generated by Django 2.2.4 on 2019-10-20 10:48

from django.db import migrations, models
import django.db.models.deletion
import three_server.base.model


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_player_lock_gold'),
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PigRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('gold', models.DecimalField(decimal_places=2, default=0.0, max_digits=19, verbose_name='积分')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.Player', verbose_name='玩家')),
            ],
            options={
                'db_table': 'announcement_pig_record',
            },
            bases=(models.Model, three_server.base.model.DictMixin),
        ),
    ]
