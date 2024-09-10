from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import os

from .models import Product

@receiver(post_save, sender=Product)
def resize_image(sender, instance, **kwargs):
    if instance.image:
        # Define the max size (width, height)
        max_size = (300, 300)

        # Open the image file using Pillow
        img = Image.open(instance.image.path)

        # Check if the image is larger than the desired size
        if img.height > max_size[0] or img.width > max_size[1]:
            # Resize the image while maintaining the aspect ratio
            img.thumbnail(max_size)
            
            # Save the resized image
            img.save(instance.image.path)
