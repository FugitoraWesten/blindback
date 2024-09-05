from django.db import models

class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)  # Optional initial description
    
    def __str__(self):
        return f"Image {self.id} - {self.uploaded_at}"

class Description(models.Model):
    image = models.ForeignKey(Image, related_name='descriptions', on_delete=models.CASCADE)
    description_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Description {self.id} for Image {self.image.id}"
