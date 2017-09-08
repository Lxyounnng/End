from myselfapp.service import v1
from app01 import models
from django.utils.safestring import mark_safe
from django.urls import reverse
class YinGunUserInfo(v1.BaseYinGunAdmin):
    def func(self,obj=None,is_headers=False):
        if is_headers:
            return '操作'
        else:
            name = "{0}:{1}_{2}_change".format(self.site.namespace, self.model_class._meta.app_label,
                                               self.model_class._meta.model_name)
            url = reverse(name, args=(obj.pk,))
            return mark_safe("<a href='{0}'>编辑</a>".format(url))


    def checkbox(self, obj=None,is_headers=False):
        if is_headers:
            return '选项'
        else:
            tag = "<input type='checkbox' value='{0}' />".format(obj.pk)
            return mark_safe(tag)
    list_display = [checkbox,'id','username','email',func]
v1.site.register(models.UserInfo,YinGunUserInfo)

class YinGunRole(v1.BaseYinGunAdmin):
    list_display = ['id','name']
v1.site.register(models.Role,YinGunRole)