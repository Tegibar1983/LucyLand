from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TouristInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_number', models.PositiveSmallIntegerField()),
                ('region_name', models.CharField(max_length=200)),
                ('capital_city', models.CharField(max_length=200)),
                ('map', models.ImageField(upload_to='map')),
                ('telephone', models.PositiveBigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
        ),
    ]
