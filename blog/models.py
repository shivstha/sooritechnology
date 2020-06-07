from django.db import models
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.CharField(max_length=50)
    # author = models.ForeignKey(User,
    #                            on_delete=models.CASCADE,
    #                            related_name='blog_posts')
    body1 = models.TextField()
    quote = models.TextField()
    body2 = models.TextField()
    time_to_read = models.IntegerField(blank=True, default=5)
    # photo = models.ImageField(upload_to='images/',
    #                           blank=False)
    image_url = models.URLField()
    publish = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail',
                       args=[self.slug])

