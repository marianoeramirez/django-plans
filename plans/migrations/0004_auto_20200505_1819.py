# Generated by Django 2.2.10 on 2020-05-05 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

PLAN_CUSTOMER_MODEL = getattr(
    settings, "PLAN_CUSTOMER_MODEL", settings.AUTH_USER_MODEL
)

PLAN_CUSTOMER_MODEL_MIGRATION_DEPENDENCY = getattr(
    settings, "PLAN_CUSTOMER_MODEL_MIGRATION_DEPENDENCY", "__first__"
)

PLAN_CUSTOMER_MODEL_DEPENDENCY = migrations.swappable_dependency(
    PLAN_CUSTOMER_MODEL
)

if PLAN_CUSTOMER_MODEL != settings.AUTH_USER_MODEL:
    PLAN_CUSTOMER_MODEL_DEPENDENCY = migrations.migration.SwappableTuple(
        (
            PLAN_CUSTOMER_MODEL.split(".", 1)[0],
            PLAN_CUSTOMER_MODEL_MIGRATION_DEPENDENCY,
        ),
        PLAN_CUSTOMER_MODEL,
    )


class Migration(migrations.Migration):
    dependencies = [
        PLAN_CUSTOMER_MODEL_DEPENDENCY,
        ('plans', '0003_make_plans_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire', models.DateField(blank=True, db_index=True, default=None, null=True, verbose_name='expire')),
                ('active', models.BooleanField(db_index=True, default=True, verbose_name='active')),
                ('customer',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=PLAN_CUSTOMER_MODEL,
                                      verbose_name='customer')),
            ],
            options={
                'verbose_name': 'User plan',
                'verbose_name_plural': 'Users plans',
            },
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='user',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='customer',
        ),
        migrations.RemoveField(
            model_name='billinginfo',
            name='user',
        ),
        migrations.AddField(
            model_name='billinginfo',
            name='customer',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE,
                                       to=PLAN_CUSTOMER_MODEL, verbose_name='customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plan',
            name='order',
            field=models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='quota',
            name='order',
            field=models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order'),
        ),
        migrations.DeleteModel(
            name='UserPlan',
        ),
        migrations.AddField(
            model_name='customerplan',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.Plan', verbose_name='plan'),
        ),
        migrations.AlterModelOptions(
            name='customerplan',
            options={'verbose_name': 'Customer plan', 'verbose_name_plural': 'Customers plans'},
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=PLAN_CUSTOMER_MODEL,
                                    verbose_name='customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=PLAN_CUSTOMER_MODEL,
                                    verbose_name='customer'),
        ),
    ]