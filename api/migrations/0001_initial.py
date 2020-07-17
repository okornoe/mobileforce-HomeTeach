# Generated by Django 3.0.8 on 2020-07-17 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Verify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.UUIDField()),
                ('authorization_code', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pending_requests', to=settings.AUTH_USER_MODEL)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings_tutor', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/')),
                ('credentials', models.FileField(blank=True, null=True, upload_to='docs/%Y/%m/%d/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/%Y/%m/%d/')),
                ('desc', models.TextField(blank=True, max_length=255, null=True)),
                ('field', models.CharField(blank=True, choices=[('SCIENCE', 'Science'), ('COMMERCIAL', 'Commercial'), ('ARTS', 'Arts'), ('ENGLISH', 'English'), ('NON_ACADEMIC', 'Non-Academic'), ('TEST_PREPARATION', 'Test Preparation'), ('OTHER', 'Other')], max_length=255)),
                ('hourly_rate', models.CharField(default=0, max_length=10000000)),
                ('major_course', models.CharField(blank=True, max_length=255, null=True)),
                ('other_courses', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, choices=[('ABUJA FCT', 'Abuja'), ('ABIA', 'Abia'), ('ADAMAWA', 'Adamawa'), ('AKWA_IBOM', 'Akwa Ibom'), ('ANAMBRA', 'Anambra'), ('BAUCHI', 'Bauchi'), ('BAYELSA', 'Bayelsa'), ('BENUE', 'Benue'), ('BORNO', 'Borno'), ('CROSS_RIVER', 'Cross River'), ('DELTA', 'Delta'), ('EBONYI', 'Ebonyi'), ('EDO', 'Edo'), ('EKITI', 'Ekiti'), ('ENUGU', 'Enugu'), ('GOMBE', 'Gombe'), ('IMO', 'Imo'), ('JIGAWA', 'Jigawa'), ('KADUNA', 'Kaduna'), ('KANO', 'Kano'), ('KATSINA', 'Kastina'), ('KEBBI', 'Kebbi'), ('KOGI', 'Kogi'), ('KWARA', 'Kwara'), ('LAGOS', 'Lagos'), ('NASSARAWA', 'Nassarawa'), ('NIGER', 'Niger'), ('OGUN', 'Ogun'), ('ONDO', 'Ondo'), ('OSUN', 'Osun'), ('OYO', 'Oyo'), ('PLATEAU', 'Plateau'), ('RIVERS', 'Rivers'), ('SOKOTO', 'Sokoto'), ('TARABA', 'Taraba'), ('YOBE', 'Yobe'), ('ZAMFARA', 'Zamfara')], max_length=255)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.ManyToManyField(blank=True, to='api.Rating')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCardInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_holder_name', models.CharField(max_length=255, null=True)),
                ('card_number', models.CharField(max_length=255, null=True)),
                ('cvv', models.CharField(max_length=255, null=True)),
                ('expiry_month', models.IntegerField(null=True)),
                ('expiry_year', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BankInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, max_length=255, null=True)),
                ('account_name', models.CharField(blank=True, max_length=255, null=True)),
                ('account_number', models.IntegerField(blank=True, null=True)),
                ('routing_number', models.IntegerField(blank=True, null=True)),
                ('social_security_number', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]