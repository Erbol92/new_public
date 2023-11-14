from django.db import models

# Create your models here.


class Urls(models.Model):
    url = models.CharField(verbose_name='url',max_length=200, null=False, blank=False, default='url' )
    sub = models.ForeignKey('self',verbose_name='корневой url', on_delete=models.CASCADE, null=True,blank=True, related_name='children')
    name = models.CharField(verbose_name='название', max_length=100, null=False, blank=False, default='name')
    class Meta:
        verbose_name = "Url"
        verbose_name_plural = "Urls"
    
    def __str__(self):
        return f'{self.name}/{self.url}'