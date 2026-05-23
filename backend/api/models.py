from django.db import models

class Book(models.Model):
    book_title = models.CharField(max_length=50, blank=False, default="Book title")
    author = models.CharField(max_length=50, blank=False, default="Author")
    image_1 = models.ImageField(upload_to="images/")
    image_2 = models.ImageField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.book_title} by  {self.author}"
    
    