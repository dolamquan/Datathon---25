from django.db import models
from django.contrib.auth.models import User

#['sex', 'cp', 'trestbps', 'chol', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# Create your models here.
class Userprofile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the built-in User model

    # Patient input fields
    age = models.FloatField()
    sex = models.IntegerField()
    cp = models.IntegerField()
    trestbps = models.FloatField()
    chol = models.FloatField()
    # fbs = models.IntegerField()
    # restecg = models.IntegerField()
    thalach = models.FloatField()
    exang = models.IntegerField()
    oldpeak = models.FloatField()
    slope = models.IntegerField()
    ca = models.FloatField()
    thal = models.IntegerField()


    # Result
    result = models.IntegerField()  # 0 = low risk, 1 = high risk
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {'High' if self.result else 'Low'} Risk on {self.created_at.date()}"