from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("legislative", "0007_auto_20181029_1527")]

    operations = [
        migrations.AlterField(
            model_name="event", name="name", field=models.CharField(max_length=1000)
        )
    ]
