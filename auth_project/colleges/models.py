from django.db import models
from django.contrib.auth.models import User
class College(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    # Academic Info
    courses = models.TextField(default="")          # ⭐ add default
    labs = models.TextField(default="")             # ⭐ add default
    gate_students = models.IntegerField(default=0)

    # Student Life
    clubs = models.TextField(default="")            # ⭐ add default
    culturals = models.TextField(default="")        # ⭐ add default

    # Career Info
    placements = models.TextField(default="")       # ⭐ add default
    top_companies = models.TextField(default="")    # ⭐ add default
    highest_package = models.CharField(max_length=50, default="Not Updated")
    average_package = models.CharField(max_length=50, default="Not Updated")

    # Fees + Media
    fees = models.CharField(max_length=100, default="Not Updated")   # ⭐ safer
    image = models.ImageField(upload_to='college_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    from django.contrib.auth.models import User

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.college.name}"

