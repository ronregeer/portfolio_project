from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        if len(self.body) > 100:
            return self.body[:100]+' ...Read More..'
        else:
            return self.body

    def eurtime(self):
        return self.pub_date.strftime('%e %b %Y')

    def __str__(self):
        return self.title
