
from itertools import count
from django import template
from UrlsApp.models import Urls
register = template.Library()

count = 0
def build_tree(url, target_obj):
    if url == target_obj:
        return {'url': url, 'children': []}
    children = url.children.all()
    for child in children:
        child_tree = build_tree(child, target_obj)
        if child_tree:
            return {'url': url, 'children': [child_tree]}
    return None

def unpack_dictionary(dictionary):
    url = dictionary['url']
    children = dictionary['children']
    global count
    count += 1
    html = f'<p>{count*"**"}<a href="{url.url}">{url.name}</a></p>'
    for child in children:
        html += unpack_dictionary(child)
        count += 1
    return html

@register.simple_tag()
def draw_menu(param:str,):
    html=''
    tree_data = []
    url_list = Urls.objects.all().order_by('sub')
    my_url = url_list.filter(name=param)
    if my_url:
        for root_url in url_list:
            tree = build_tree(root_url, my_url.first())
            if tree:
                tree_data.append(tree)
                break
        dict_list = tree_data[0]['children']
        main = tree_data[0]["url"]
        html += f'<p><a href="{main.url}">{main.name}</a></p>'
        for dictionary in dict_list:
            html += unpack_dictionary(dictionary)
            global count
            count = 0
    else:
        html = '<p> нет такого url </p>'
    return html
