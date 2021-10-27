from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

CATEGORY = (
    ('cars', 'Cars'),
    ('IT', 'IT'),
    ('city', 'City')
)

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=100)
    image = models.ImageField('Картинка', upload_to='')
    description = models.TextField('Описание')
    category = models.CharField('Категория', max_length = 200, choices=CATEGORY)
    date_pub = models.DateTimeField(auto_now_add=True)
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(100, 50)],
                                    format='JPEG',
                                    options={'quality': 60})

    


    def __str__(self):
        return self.title