from django.db import models
from django.contrib.gis.db import models

class Points(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=10)
    x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom_point = models.PointField(blank=True, null=True, spatial_index=True)

    def __str__(self):
        return str(self.geom_point)

    def as_json(self):
        return dict(
        input_id=self.id, input_x=self.x, input_y=self.y, input_geom_point=self.geom_point
        )

    class Meta:
        verbose_name_plural = "Points"
        managed = False
        db_table = 'points'
