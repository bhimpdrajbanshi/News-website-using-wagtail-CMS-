from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    template='home/home_page.html'
    body = models.CharField(
        max_length=120
    )
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
