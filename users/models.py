from django.db import models
from datetime import datetime
from PIL import Image

class User(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  image = models.ImageField(default='default.jpg', upload_to='profile_pics')
  def __str__(self):
        return f'{self.user.username} Profile'

  def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name