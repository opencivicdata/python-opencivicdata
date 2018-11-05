from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislative', '0006_billversion_extras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=1000),
        ),
    ]
