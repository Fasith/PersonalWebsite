# Generated by Django 2.2.1 on 2019-06-21 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190621_0647'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_description', models.CharField(max_length=500)),
                ('Image', models.ImageField(upload_to='carousel_images/')),
            ],
        ),
    ]
