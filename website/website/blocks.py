# -*- coding: utf-8 -*-
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailcore.blocks import (
    PageChooserBlock, CharBlock, ChoiceBlock, 
    RichTextBlock, StreamBlock, StructBlock, 
    TextBlock, ListBlock,
)

from wagtail.wagtailsnippets import blocks as sb

from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore import blocks

#from wagtailblocks_cards.blocks import CardsBlock



class SubscribeBlock(StructBlock):
	h3 = blocks.CharBlock(required=False)
	text = blocks.CharBlock(required=False)
	btntext = blocks.CharBlock(required=False)
	smalltext = blocks.CharBlock(required=False)
	handle = blocks.CharBlock()

	#class Meta:
	#	icon = 'site'
	#	template = "sections/subscribe_block.html"


class HomeCarouselBlock(blocks.StreamBlock):
	color = blocks.CharBlock()
	image = ImageChooserBlock()

	quotation = blocks.StructBlock([
		('text', blocks.TextBlock()),
		('author', blocks.CharBlock()),
	])

	video = EmbedBlock()

	class Meta:
		icon='cogs'

class BaseStreamBlock(StreamBlock):
	subscribe_block = SubscribeBlock()

