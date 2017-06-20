from lxml import html
import requests
import json

import click

@click.command()
@click.argument('query_str')
def scrape(query_str):
    r = requests.get('https://duckduckgo.com/html?q={}'.format(query_str))
    document = html.fromstring(r.content)
    result_els = document.xpath('//div[contains(@class, "result")]')


    number_results = len(result_els)

    click.echo(number_results)

    results = []
    for result in result_els:
        title       = result.xpath('//div[contains(@class, "links_main")]/h2[contains(@class, "result__title")]/a//text()')
        description = result.xpath('//div[contains(@class, "links_main")]/a[contains(@class, "result__snippet")]//text()')
        url         = result.xpath('//div[contains(@class, "links_main")]/h2[contains(@class, "result__title")]/a//@href')
        results.append({
            'title': title,
            'description': description,
            'url': url,
        })

    output = json.dumps({
        'search_term': query_str,
        'result_count': number_results,
        'results': results,
    })

    click.echo(output)

if __name__ == '__main__':
    scrape()
