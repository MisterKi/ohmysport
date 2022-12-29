from django.db import models
from django.utils.text import slugify


class Sport(models.Model):
    name = models.CharField(max_length=150)
    federation = models.CharField(max_length=150)
    description = models.TextField()
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Sport'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True)
    president = models.CharField(max_length=150)
    manager = models.CharField(max_length=150)
    name_of_field = models.CharField(max_length=150)
    description = models.TextField()
    image_link = models.TextField()
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Team'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    teams = models.ManyToManyField(Team)
    date = models.DateField()
    slug = models.SlugField()
    image_link = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
