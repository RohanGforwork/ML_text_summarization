from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=128, unique=True)  # Firebase UID
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class UserDataset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dataset = models.FileField(upload_to='datasets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)