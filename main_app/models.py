from django.db import models
from django.urls import reverse
from datetime import date

CONDITION = (
  ('B', 'Blunt'),
  ('C', 'Correction Needed'),
  ('H', 'Honing/Maintenance'),
)


class Accessory(models.Model):
  name = models.CharField(max_length=50)
  purpose= models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('accessories_detail', kwargs={'pk': self.id})



class Knife(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=300)
    description = models.TextField(max_length=1500)
    size = models.IntegerField()
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'knife_id': self.id})
    
    def sharp_for_today(self):
        return self.sharpening_set.filter(date=date.today()).count() >= len(CONDITION)

class Sharpening(models.Model):
  date = models.DateField('Sharpening Date')
  condition = models.CharField(
    max_length=1,
    choices=CONDITION,
    default=CONDITION[0][0]
  )

  # Create a cat_id FK
  knife = models.ForeignKey(
    Knife,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_condition_display()} on {self.date}"

  class Meta:
     ordering = ['-date']