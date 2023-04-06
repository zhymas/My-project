from django.db import models

class Article(models.Model):
    title = models.CharField("Название", max_length=50)
    anons = models.CharField('Анонс', max_length=100)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/%2Fnews{self.id}"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
