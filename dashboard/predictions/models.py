from django.db import models

class CustomerPredictions(models.Model):
    customer_id = models.CharField(max_length=50, blank=True, null=True)
    will_purchase = models.IntegerField(blank=True, null=True)
    prediction = models.IntegerField(blank=True, null=True)
    probability_no_purchase = models.FloatField(blank=True, null=True)
    probability_purchase = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_predictions'