from django.db import models
from datetime import datetime


class Table(models.Model):
    index = models.IntegerField(blank=True, null=False, primary_key=True)
    name = models.TextField(blank=True, null=True)
    serving_wt = models.FloatField(blank=True, null=True)
    kcal = models.FloatField(blank=True, null=True)
    carbo = models.TextField(blank=True, null=True)
    protein = models.TextField(blank=True, null=True)
    fat = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Table'

    def __str__(self):
        return self.name


# class Food(models.Model):
#     foodName = models.TextField("음식명", max_length=100)
#     # 그램,
#     SERVING_WT = models.CharField("그램수", max_length=100)
#     NUTR_CONT1 = models.CharField("칼로리", max_length=100)
#     NUTR_CONT2 = models.CharField("탄수화물", max_length=100)
#     NUTR_CONT3 = models.CharField("단백질", max_length=100)
#     NUTR_CONT4 = models.CharField("지방", max_length=100)
#
#     def __str__(self):
#         return self.foodName
#

