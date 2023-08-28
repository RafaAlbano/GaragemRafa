# Generated by Django 4.2.4 on 2023-08-28 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0002_veiculo_capa"),
    ]

    operations = [
        migrations.CreateModel(
            name="Modelo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="modelos",
                        to="garagem.categoria",
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="modelos",
                        to="garagem.marca",
                    ),
                ),
            ],
            options={
                "verbose_name": "Modelo",
                "verbose_name_plural": "Modelos",
            },
        ),
    ]