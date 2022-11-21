from django.db import models
import uuid


class Project(models.Model):   ## Class is created to let know its not ordinary class
   title = models.CharField(max_length = 200)
   description = models.TextField(null = True, blank=True)
   demo_link = models.CharField(max_length = 2000, blank = True, null = True)
   featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
   source_link = models.CharField(max_length = 2000, blank = True, null = True)
   tags = models.ManyToManyField('Tag', blank=True)
   vote_total = models.IntegerField(default=0, null=True, blank=True)
   vote_ratio = models.IntegerField(default=0, null=True, blank=True)
   created = models.DateTimeField(auto_now_add = True)
   id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

   def __str__(self):
      return self.title


class Review(models.Model):
   VOTE_TYPE = (
      ('up','Up Vote'),
      ('down', 'Down Vote')
   )
   # owner =
   projects = models.ForeignKey(Project, on_delete=models.CASCADE)  ##what on_null do??
   body = models.TextField(max_length=2000, null=True, blank = False)
   value = models.CharField(max_length=200, choices=VOTE_TYPE)
   created =models.DateTimeField(auto_now_add=True)
   id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

   def __str__(self):
      return self.value


class Tag(models.Model):
   name = models.CharField(max_length=30 )
   created = models.DateTimeField(auto_now_add=True)
   id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

   def __str__(self):
      return self.name


