

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0008_auto_20200425_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='public_key_n',
            field=models.BigIntegerField(default=0),
        ),
    ]
