from django.db import models

class Concept(models.Model):
    concept_title = models.CharField(max_length=180)
    concept_text = models.CharField(max_length=1024)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.concept_title
