from django import template
from menuapp.models import MenuItem

register = template.Library()


@register.inclusion_tag('include/menu_items.html')
def draw_menu(menu_name, request):
    menu = MenuItem.objects.filter(menu_name=menu_name).prefetch_related('children').first()
    if menu:
        return {'menu_items': menu.get_descendants(), 'main_menu': menu, 'request': request}
    return {'menu_items': []}
