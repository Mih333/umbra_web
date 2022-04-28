from cms.models.pluginmodel import CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerFileField, FilerImageField
from easy_thumbnails.files import get_thumbnailer
from django.utils.translation import gettext_lazy as _

OPTION_1 = (
    ('0%', _('Puff 0%')),
    ('2%', _('Puff 2%')),
    ('50g', _('Hookah 50g')),
    ('200g', _('Hookah 200g')),
)

OPTION_2 = (
    ('400', _('Puff 400')),
    ('600', _('Puff 600')),
    ('1000', _('Puff 1000')),
    ('2000', _('Puff 2000')),
    ('classic', _('UMBRA Classic')),
    ('intense', _('UMBRA Intense')),
)

class Product(CMSPlugin):
    name = models.CharField(
        max_length=100,
        help_text=_("Product name"),
        null=True, blank=False
        )    
    option_1 = models.CharField(
        verbose_name=_('Indices for Nicotine & Grammage'),
        choices=OPTION_1,
        blank=True,
        max_length=255,
        default='',
        )
    option_2 = models.CharField(
        verbose_name=_('Choose category'),
        choices=OPTION_2,
        blank=True,
        max_length=255,
        default='',
        )
    image = FilerImageField(
        verbose_name=_("product image"),
        blank=True,
        null=True,
        related_name=_("product_image"),
        on_delete=models.SET_NULL
        )
    description = models.TextField(
        max_length=350,
        help_text=_("Product description"),
        null=True, blank=True
        )
    
    def __str__(self):
        return self.name or str(self.pk)