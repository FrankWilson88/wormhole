from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
  (0, 'Draft'),
  (1, 'Publish'),
)

class Article(models.Model):
  articleID = models.SlugField(max_length=200, unique=True)
  title = models.CharField(max_length=25, default="Title", null=False, blank=False)
  createdOn = models.DateTimeField(auto_now_add=True)
  createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
  updatedOn = models.DateTimeField(auto_now=True)
  content = models.TextField(null=False, blank=False, default="Article Content")
  img1 = models.ImageField(upload_to='article/', null=True, blank=True)
  img2 = models.ImageField(upload_to='article/', null=True, blank=True)
  img3 = models.ImageField(upload_to='article/', null=True, blank=True)
  img4 = models.ImageField(upload_to='article/', null=True, blank=True)
  img5 = models.ImageField(upload_to='article/', null=True, blank=True)
  status = models.IntegerField(choices=STATUS, default=0)
  class Meta:
    ordering = ['createdOn']
  def __str__(self):
    return f'{self.articleID} {self.title} {self.createdOn} {self.createdBy} {self.updatedOn}'