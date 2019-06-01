import secrets
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Project(models.Model):

    name = models.CharField(max_length=250)
    workspace = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(max_length=250)
    users = models.ManyToManyField(User, blank=True)
    token = models.CharField(max_length=48)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = secrets.token_urlsafe(48)
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)


class Action(models.Model):

    name = models.CharField(max_length=250)
    endpoint = models.CharField(max_length=250)
    script = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
