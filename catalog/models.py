from django.db import models


class VideoCatalog(models.Model):
    catalog_number = models.CharField(max_length=30, verbose_name="№ каталога")
    performer = models.CharField(max_length=30, verbose_name="Исполнитель")
    title = models.CharField(max_length=30, verbose_name="Название")
    duration = models.DurationField(verbose_name="Хронометраж", blank=True, null=True)
    video_type = models.CharField(max_length=30, verbose_name="Тип", blank=True, null=True)
    director = models.CharField(max_length=30, verbose_name="Режиссёр", blank=True, null=True)
    screenwriter = models.CharField(max_length=30, verbose_name="Сценарист", blank=True, null=True)
    composer = models.CharField(max_length=30, verbose_name="Композитор", blank=True, null=True)
    year = models.PositiveIntegerField(verbose_name="Год", blank=True, null=True)
    youtube_link = models.URLField(verbose_name="Youtube", blank=True, null=True)
    rutube_link = models.URLField(verbose_name="RuTube", blank=True, null=True)
    yandex_link = models.URLField(verbose_name="Яндекс", blank=True, null=True)
    vk_link = models.URLField(verbose_name="VK", blank=True, null=True)
    zen_link = models.URLField(verbose_name="Дзен", blank=True, null=True)
    upc = models.CharField(max_length=30, verbose_name="UPC", blank=True, null=True)
    files = models.FileField(blank=True, null=True, verbose_name='Файлы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Видеокаталог"
        verbose_name_plural = "Видеокаталоги"
