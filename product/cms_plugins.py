from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from .models import Product

@plugin_pool.register_plugin
class ProductPlugin(CMSPluginBase):
    model = Product
    name = _("Product")
    render_template = "products.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
