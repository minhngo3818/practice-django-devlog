from django.db import models
import uuid
from users.models import Profile


# Create your models here.
# Models is used for manipulate data from database
class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #                                ^           ^
    #                       can be empty        django knows
    #                       in database         it can be blank
    featured_image = models.ImageField(
        null=True, blank=True)
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    src_link = models.CharField(max_length=1000, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)   # a string 'Tag' to avoid in-order-code error
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title
    # Note: Create a str representation for title+uuid display on admin
    # Only return a title of added project

    # Note:
    # auto_now=True update time whenever there is a modification
    # auto_now_add=True update time whenever an instance is created
    @property
    def imageURL(self):
        try:
            img_url = self.featured_image.url
        except:
            img_url = ''

        return img_url


class Review(models.Model):

    # Drop down menu
    VOTE_TYPE = (
        ('up', 'up'),
        ('down', 'down')
    )

    # owner
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    # on_delete: what happen to instance of Review when Project is deleted
    #       -> SET_NULL: project is null, reviews remain
    #       -> CASCADE: project is null, reviews are deleted

    # related_name='reviews': set reviews with a name value for convieniently access as obj .reviews.all()

    # Set a relationship between objects in database
    body = models.TextField(null=True, blank=True)

    # Value of votes
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
