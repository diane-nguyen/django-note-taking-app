from django.db import models

# This represents each note user inputs
# in note taking app
class eachNote(models.Model):
    content = models.TextField()