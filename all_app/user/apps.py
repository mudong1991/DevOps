from django.apps import AppConfig
from django.db.models.signals import post_migrate


class UserConfig(AppConfig):
    name = 'user'
    verbose_name = "用户中心"

    def ready(self):
        from user.signals import thread_init, modified_permission
        post_migrate.connect(receiver=thread_init, sender=self, dispatch_uid='all_app.user.signals.thread_init')
        # post_migrate.connect(receiver=create_permissions, dispatch_uid='all.user.signals.create_permissions')
        post_migrate.connect(receiver=modified_permission, dispatch_uid='all.user.signals.modified_permission')