from django.apps import AppConfig


class MyselfappConfig(AppConfig):
    name = 'myselfapp'
    def ready(self):
        super(MyselfappConfig,self).ready()

        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('yg')
