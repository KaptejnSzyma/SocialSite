from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

import misaka

from groups.models import Group
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username,
<<<<<<< HEAD
                                               'pk': self.pk})
=======
                                               'pk': self.pk}
>>>>>>> ff6df5c1fed95878fb0fafba06969f6a6c6ff3d3
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']
