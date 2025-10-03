from __future__ import annotations
import uuid
from django.db import models
from django.utils import timezone


class UUIDModel(models.Model):
    """Primárny kľúč ako UUID v každej doménovej tabuľke."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """Automatické timestamps + index na created_at pre rýchle sortovanie."""
    created_at = models.DateTimeField(default=timezone.now, db_index=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    """
    Soft delete príznak (nepoužívaj FOREIGN KEY CASCADE, rieš biznisovo).
    QuerySety vo vlastných manageroch môžu filtrovať is_deleted=False.
    """
    is_deleted = models.BooleanField(default=False, db_index=True)

    class Meta:
        abstract = True

    def soft_delete(self) -> None:
        if not self.is_deleted:
            self.is_deleted = True
            self.save(update_fields=["is_deleted", "updated_at"] if hasattr(self, "updated_at") else ["is_deleted"])


class BaseModel(UUIDModel, TimeStampedModel):
    """Najčastejší základ — UUID + timestamps."""
    class Meta:
        abstract = True