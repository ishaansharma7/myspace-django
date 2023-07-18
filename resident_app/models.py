from django.db import models
from django.db import models


class Resident(models.Model):
    resident_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    email_id = models.EmailField()
    resident_building_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    token_amount = models.DecimalField(max_digits=10, decimal_places=2)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    move_in_date = models.DateField()
    move_out_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.resident_name
