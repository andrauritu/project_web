from django.db import models

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    your_project_title = models.CharField(max_length=200, default="")
    your_colleagues_for_the_project = models.TextField(default="")
    email = models.EmailField()
    project_link = models.URLField(max_length=500, blank=True, default="")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"