from django.conf import settings
from appconf import AppConf


class MultiuploaderConf(AppConf):
    THUMBNAIL_ALIASES = {
        '': {
            'fileupload': {'size': (70, 70), 'crop': True},
        },
    }
