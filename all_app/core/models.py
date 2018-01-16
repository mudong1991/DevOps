from django.db import models


class CoreManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def get_deleted_queryset(self):
        return super().get_queryset().filter(is_deleted=True)


class CoreModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_deleted = models.BooleanField(default=False, verbose_name='是否已删除', editable=False)
    objects = CoreManager()

    class Meta:
        abstract = True
