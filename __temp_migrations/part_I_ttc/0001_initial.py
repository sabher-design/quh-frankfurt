# Generated by Django 2.2.12 on 2024-07-11 15:07

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part_i_ttc_group', to='otree.Session')),
            ],
            options={
                'db_table': 'part_I_ttc_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='part_i_ttc_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'part_I_ttc_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('ctrq1_ttc', otree.db.models.IntegerField(null=True, verbose_name='Wie viele Schüler:innen bewerben sich für einen Schulplatz?')),
                ('ctrq2_ttc', otree.db.models.IntegerField(null=True, verbose_name='Wie viele Plätze bleiben übrig, sobald alle Schüler:innen an einer Schule zugelassen wurden?')),
                ('time_left', otree.db.models.IntegerField(default=300, null=True)),
                ('ctrq3_ttc_blue', otree.db.models.StringField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=10000, null=True, verbose_name='')),
                ('ctrq3_ttc_yellow', otree.db.models.StringField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=10000, null=True, verbose_name='')),
                ('ctrq3_ttc_orange', otree.db.models.StringField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=10000, null=True, verbose_name='')),
                ('ctrq3_ttc_purple', otree.db.models.StringField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=10000, null=True, verbose_name='')),
                ('mc1_ttc', otree.db.models.StringField(choices=[('Richtig', 'Richtig'), ('Falsch', 'Falsch')], max_length=10000, null=True, verbose_name='1. Bei der Entscheidung, welche Präferenzliste man an die zentrale Zulassungsstelle übermittelt, sollte man darauf achten, dass man sich nicht bei der beliebtesten Schule zuerst bewirbt.')),
                ('mc2_ttc', otree.db.models.StringField(choices=[('Richtig', 'Richtig'), ('Falsch', 'Falsch')], max_length=10000, null=True, verbose_name='2. Es ist ausschlaggebend für die Erstellung der eigenen Präferenzliste, die Wertetabelle für alle anderen Schüler:innen zu kennen.')),
                ('mc3_ttc', otree.db.models.StringField(choices=[('Richtig', 'Richtig'), ('Falsch', 'Falsch')], max_length=10000, null=True, verbose_name='3. Das Zulassungsverfahren ist so konstruiert, dass die übermittelte Präferenzliste immer mit der Reihenfolge übereinstimmen sollte, die sich aus der Wertetabelle ergibt.')),
                ('mc4_ttc', otree.db.models.StringField(choices=[('Richtig', 'Richtig'), ('Falsch', 'Falsch')], max_length=10000, null=True, verbose_name='4. Ihre Präferenzliste sollte nur mit der Reihenfolge aus der Wertetabelle übereinstimmen, wenn Sie sicher sind, dass alle Schüler:innen ebenso verfahren.')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='part_I_ttc.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part_i_ttc_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part_i_ttc_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part_I_ttc.Subsession')),
            ],
            options={
                'db_table': 'part_I_ttc_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part_I_ttc.Subsession'),
        ),
    ]
