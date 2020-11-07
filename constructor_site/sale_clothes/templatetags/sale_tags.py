from django import template
from sale_clothes.models import AdditionalData

register = template.Library()

@register.simple_tag
def get_additional_data(element_id):
	additional_data = AdditionalData.objects.filter(
		element_id=element_id).first()
	return additional_data

@register.simple_tag
def get_good_limit(list_goods, limit):
	return list_goods[:limit]