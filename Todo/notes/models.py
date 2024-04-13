from django.db import models

class Notes(models.Model):
    executor = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    dateoflsu = models.DateTimeField()
    def __str__(self):
        return f"{self.title}"

class Commentary(models.Model):
    nickname = models.CharField(max_length=100)
    commentary = models.TextField()
    date = models.DateTimeField()
    pk_note = models.IntegerField()
    def __str__(self):
        return f"{self.nickname}"
