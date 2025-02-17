from django.db import models
from commons.models import (
    OrgModelMixins,
    TimeStampMixins
)
from accounts.models import User


class QuickBillDetails( OrgModelMixins, TimeStampMixins, models.Model):
    """
    This is the model to store the details of quick bill by the user
    """

    customer_name = models.CharField(max_length=256, blank=True, null=True)
    customer_addr = models.CharField(max_length=256, blank=True, null=True)
    customer_email = models.CharField(max_length=256, blank=True, null=True)
    customer_phone = models.CharField(max_length=256, blank=True, null=True)
    bill_id = models.CharField(max_length=256, blank=True, null=True)
    bill_total = models.CharField(max_length=256, blank=True, null=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="quick_biller"
    )
