# Generated by Django 2.2.1 on 2019-05-22 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100, unique=True)),
                ('album', models.CharField(max_length=100, unique=True)),
                ('content', models.CharField(max_length=150)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subreview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rrr', to='reviews.Review')),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rrr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]