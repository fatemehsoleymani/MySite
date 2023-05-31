from django.contrib.sitemaps import Sitemap
from .models import Post


def lastmod(obj):
    return obj.update_date


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'http'

    def items(self):
        return Post.published.all()
