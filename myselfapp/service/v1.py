from django.shortcuts import render, HttpResponse
class BaseYinGunAdmin(object):
    def __init__(self, model_class, site):
        self.model_class = model_class
        self.site = site

    @property
    def urls(self):
        from django.conf.urls import url, include
        info = self.model_class._meta.app_label,self.model_class._meta.model_name
        urlpatterns = [
            url(r'^$', self.changelist_view,name='%s_%s_changelist' %info),
            url(r'^add/$', self.add_view,name='%s_%s_add' %info),
            url(r'^(.+)/delete/$', self.delete_view,name='%s_%s_delete' %info),
            url(r'^(.+)/change/$', self.change_view,name='%s_%s_change' %info),
        ]
        return urlpatterns

    def changelist_view(self,request):
        self.request = request
        result_list = self.model_class.objects.all()
        context = {
            'result_list':result_list,
            'list_display':self.list_display,
            'ygadmin_obj':self
        }
        return render(request,'yg/change_list.html',context)
    def add_view(self,request):
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        data = '%s_%s_add' % info
        return HttpResponse(data)
    def delete_view(self,request,pk):
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        data = '%s_%s_del' % info
        return HttpResponse(data)
    def change_view(self,request,pk):
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        data = '%s_%s_change' % info
        return HttpResponse(data)

class YinGunSite(object):
    def __init__(self):
        self._registry = {}
        self.namespace = 'myselfapp'
        self.app_name = 'myselfapp'

    def register(self, model_class, base=BaseYinGunAdmin):
        self._registry[model_class] = base(model_class, self)

    def get_urls(self):
        from django.conf.urls import url, include
        ret = []
        for model_cls, myselfapp_admin_obj in self._registry.items():
            app_label = model_cls._meta.app_label
            model_name = model_cls._meta.model_name
            ret.append(url(r'^%s/%s/' % (app_label, model_name), include(myselfapp_admin_obj.urls)))
        return ret

    @property
    def urls(self):
        return self.get_urls(), self.app_name, self.namespace

    def login(self, request):
        return HttpResponse('login')

    def logout(self, request):
        return HttpResponse('logout')


site = YinGunSite()
