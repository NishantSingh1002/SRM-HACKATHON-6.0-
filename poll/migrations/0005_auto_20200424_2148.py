

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_block'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('private_key', models.CharField(max_length=200)),
                ('has_voted', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Block',
        ),
    ]
