# Generated by Django 2.2.2 on 2019-06-22 03:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('title', models.CharField(max_length=100, null=True)),
                ('is_private', models.BooleanField(default=True)),
            ],
            bases=('app.base',),
        ),
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('filename', models.URLField(unique=True)),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Album')),
            ],
            bases=('app.base',),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('filename', models.ImageField(default='image.jpg', upload_to='photos/')),
                ('thumbnail', models.ImageField(default='thumbnail.jpg', upload_to='thumbnails/')),
                ('albums', models.ManyToManyField(to='app.Album')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('app.base',),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('is_expired', models.BooleanField(default=False)),
                ('url', models.URLField(unique=True)),
                ('archive_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Archive')),
            ],
            bases=('app.base',),
        ),
        migrations.AddField(
            model_name='album',
            name='archive_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Archive'),
        ),
        migrations.AddField(
            model_name='album',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
