#!/usr/bin/env python
import feedparser

from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

def render_template(data, template_name, filters=None):
    """Render data using a jinja2 template"""
    env = Environment(loader=FileSystemLoader(''))

    if filters is not None:
        for key, value in filters.iteritems():
            env.filters[key] = value

    template = env.get_template(template_name)
    return template.render(feed=data).encode('utf-8')

def main():
    feed = feedparser.parse('http://www.astrazeneca.com/cs/Satellite?c=AZ_Placeholder_C&childpagename=astrazeneca%2FAZ_Placeholder_C%2FRSS&cid=1277293175128&p=1277293173773&packedargs=item-alias%3DLatestPressReleasesHubBlock%26item-context%3DHome&pagename=AZ%2FWrapper')

    json = render_template(feed.entries, 'news.tmpl')

    with open('../news.json', 'w') as output:
        output.write(json)

if __name__ == '__main__':
    main()