# Generated by Django 2.2.7 on 2019-12-28 07:38

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PRO', 'Profesor'), ('EST', 'Estudiante'), ('EXT', 'Externo')], max_length=20, verbose_name='tipo')),
                ('document_id', models.IntegerField(unique=True, verbose_name='cédula')),
                ('first_name_1', models.CharField(max_length=100, verbose_name='primer nombre')),
                ('first_name_2', models.CharField(blank=True, max_length=100, null=True, verbose_name='segundo nombre')),
                ('last_name_1', models.CharField(max_length=100, verbose_name='primer apellido')),
                ('last_name_2', models.CharField(blank=True, max_length=100, null=True, verbose_name='segundo apellido')),
                ('ucab_mail', models.CharField(blank=True, max_length=100, null=True, verbose_name='correo ucab')),
                ('personal_mail', models.CharField(max_length=100, verbose_name='correo personal')),
                ('phone_1', models.CharField(max_length=15, verbose_name='teléfono 1')),
                ('phone_2', models.CharField(blank=True, max_length=15, null=True, verbose_name='teléfono 2')),
                ('observations', models.CharField(blank=True, max_length=500, null=True, verbose_name='observaciones')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateTimeField(verbose_name='fecha de entrega')),
                ('title', models.CharField(max_length=200, verbose_name='título')),
                ('academic_tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_tutor_proposal', to='managerApp.Person', verbose_name='tutor académico')),
                ('company_tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_tutor_proposal', to='managerApp.Person', verbose_name='tutor_empresarial')),
            ],
            options={
                'verbose_name': 'Propuesta',
                'verbose_name_plural': 'Propuestas',
            },
        ),
        migrations.CreateModel(
            name='ProposalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Estado de propuesta',
                'verbose_name_plural': 'Estados de propuestas',
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='código terminología (Ej:201915)')),
                ('description', models.CharField(max_length=50, verbose_name='descripción')),
            ],
            options={
                'verbose_name': 'Terminología',
                'verbose_name_plural': 'Terminologías',
            },
        ),
        migrations.CreateModel(
            name='ThesisStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Estado de tesis',
                'verbose_name_plural': 'Estados de tesis',
            },
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='título')),
                ('nrc', models.IntegerField(verbose_name='código NRC')),
                ('descriptors', models.CharField(max_length=50, verbose_name='descriptores')),
                ('thematic_category', models.CharField(max_length=50, verbose_name='categoría temática')),
                ('top_date', models.DateTimeField(verbose_name='fecha tope de entrega')),
                ('company_name', models.CharField(max_length=100, verbose_name='nombre de la empresa')),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thesis_proposal', to='managerApp.Proposal', verbose_name='propuesta asociada')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_thesis', to='managerApp.ThesisStatus', verbose_name='estatus')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='term_thesis', to='managerApp.Term', verbose_name='terminología')),
            ],
            options={
                'verbose_name': 'Tesis',
                'verbose_name_plural': 'Tesis',
            },
        ),
        migrations.AddField(
            model_name='proposal',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_proposal', to='managerApp.ProposalStatus', verbose_name='estatus de la propuesta'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='student_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_1_proposal', to='managerApp.Person', verbose_name='estudiante 1'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='student_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_2_proposal', to='managerApp.Person', verbose_name='estudiante 2'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='term_proposal', to='managerApp.Term', verbose_name='terminología en la que fue entregada'),
        ),
        migrations.CreateModel(
            name='Defense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defense_date', models.DateTimeField(verbose_name='fecha de la defensa')),
                ('jury_1_assistance_confirmation', models.BooleanField(default=False, verbose_name='jurado 1 asiste')),
                ('jury_2_assistance_confirmation', models.BooleanField(default=False, verbose_name='jurado 2 asiste')),
                ('jury_3_assistance_confirmation', models.BooleanField(default=False, verbose_name='jurado 3 asiste')),
                ('grade', models.IntegerField(verbose_name='calificación')),
                ('publication_mention', models.BooleanField(default=False, verbose_name='mención publicación')),
                ('honorific_mention', models.BooleanField(default=False, verbose_name='mención honorífica')),
                ('corrections_delivered', models.BooleanField(default=False, verbose_name='se entregaron correcciones')),
                ('top_date_corrections', models.DateTimeField(verbose_name='fecha tope de correcciones')),
                ('grade_uploaded', models.BooleanField(default=False, verbose_name='se subió la calificación')),
                ('observations', models.CharField(blank=True, max_length=500, null=True, verbose_name='observaciones')),
                ('thesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thesis_defense', to='managerApp.Thesis', verbose_name='tesis asociada')),
            ],
            options={
                'verbose_name': 'Defensa',
                'verbose_name_plural': 'Defensas',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_manager', models.BooleanField(default=False)),
                ('is_guest', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
