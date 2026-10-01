from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10)),
                ('course', models.CharField(choices=[('BTech AI & DS', 'BTech AI & DS'), ('BTech CSE', 'BTech CSE'), ('BTech IT', 'BTech IT'), ('BTech ECE', 'BTech ECE'), ('Other', 'Other')], max_length=50)),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
