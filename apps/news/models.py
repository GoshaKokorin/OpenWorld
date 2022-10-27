from django.db import models


class News(models.Model):
    title = models.CharField('title', max_length=255)
    description = models.TextField('description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Images(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    src = models.ImageField('image', upload_to='images/news/')

    class Meta:
        verbose_name = 'Картинки'
        verbose_name_plural = 'Картинки'
