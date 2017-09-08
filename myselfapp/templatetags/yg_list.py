from django.template import Library
from types import FunctionType

register = Library()

def table_body(result_list,list_display,ygadmin_obj):
    for row in result_list:
        yield [ name(ygadmin_obj,obj=row) if isinstance(name,FunctionType) else getattr(row, name)  for name in list_display]

def table_head(list_display,ygadmin_obj):
    for title in list_display:
        if isinstance(title,FunctionType):
            yield title(ygadmin_obj,is_headers=True)
        else:
            yield ygadmin_obj.model_class._meta.get_field(title).verbose_name

@register.inclusion_tag("yg/md.html")
def func(result_list,list_display,ygadmin_obj):
    body = table_body(result_list,list_display,ygadmin_obj)
    head = table_head(list_display,ygadmin_obj)
    return {'data':body,'title':head}

