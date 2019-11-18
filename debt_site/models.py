from django.db import models  # type: ignore


class Debt(models.Model):  # type: ignore

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    debt_amount = models.IntegerField()
