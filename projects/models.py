from django.db import models
import uuid

class Project(models.Model):
    id  = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    project_image = models.ImageField(null=True, blank=True, default='testlogo.png')
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_code = models.CharField(max_length=2000, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    vote_count = models.IntegerField(default=0, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    VOTE_CHOISE = [
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    ]
    id  = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # owner = 
    description = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=2000, choices=VOTE_CHOISE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.value

class Tag(models.Model):
    id  = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title