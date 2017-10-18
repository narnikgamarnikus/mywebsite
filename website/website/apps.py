from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'website.website'
    verbose_name = "Website"

    def ready(self):
        pass