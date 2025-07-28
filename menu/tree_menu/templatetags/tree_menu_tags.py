from django import template
from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_items': [], 'active_ids': set()}

    items = MenuItem.objects.filter(menu=menu).select_related('parent').order_by('order')
    items_by_id = {item.id: item for item in items}
    children_map = {}

    for item in items:
        children_map.setdefault(item.parent_id, []).append(item)

    def build_tree(parent_id=None):
        return [
            {
                'item': item,
                'children': build_tree(item.id)
            }
            for item in children_map.get(parent_id, [])
        ]

    active_item = None
    for item in items:
        if item.get_url() == current_path:
            active_item = item
            break

    active_ids = set()
    if active_item:
        parent = active_item.parent
        while parent:
            active_ids.add(parent.id)
            parent = parent.parent
        active_ids.add(active_item.id)

    return {
        'menu_items': build_tree(),
        'active_ids': active_ids,
        'active_item_id': active_item.id if active_item else None,
    }
