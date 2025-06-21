from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Achievement(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    birth_year = models.IntegerField(blank=True, null=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cats'
        )
    achievement = models.ManyToManyField(Achievement, through='AchievementCat')
    def __str__(self):
        return self.name
    
class AchievementCat(models.Model):
    name = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}  {self.cat}'