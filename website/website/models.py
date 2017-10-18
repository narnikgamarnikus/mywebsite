from django.db import models

from django.utils import six
from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable, PageBase
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (
	MultiFieldPanel, FieldPanel, InlinePanel, StreamFieldPanel,
)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from wagtailmenus.models import MenuPage

from wagtailmetadata.models import MetadataPageMixin

from .blocks import BaseStreamBlock

from modelcluster.contrib.taggit import ClusterTaggableManager


from wagtail.wagtailcore.fields import RichTextField, StreamField


class HomePage(six.with_metaclass(PageBase, MetadataPageMixin, MenuPage)):

	head = models.CharField(max_length=255)
	text = models.CharField(max_length=255)
	#tags = ClusterTaggableManager(through=FAQTag, blank=True)

	body = StreamField(
		BaseStreamBlock(),
		verbose_name="Блоки для главной страницы", blank=True
	)

	content_panels = [
		FieldPanel('title'),
		FieldPanel('head'),
		FieldPanel('text'),
		StreamFieldPanel('body'),

	]

	panels = [
		StreamFieldPanel('body'),
	]

	#promote_panels = Page.promote_panels + [
	#	FieldPanel('tags'),
	#]

	def __str__(self):
		return '{}'.format(self.head)