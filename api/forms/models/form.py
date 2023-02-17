from django.db import models


class FormData(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    number_of_travellers = models.IntegerField()
    budget_per_person = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["email"]),
            models.Index(fields=["destination"]),
            models.Index(fields=["number_of_travellers"]),
            models.Index(fields=["budget_per_person"]),
        ]
