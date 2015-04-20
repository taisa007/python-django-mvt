from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField('title', max_length=255)
    contents = models.TextField('contents')

    def __str__(self):
        return "<Entry('%s','%s', '%s')>" % (self.id, self.title, self.contents)