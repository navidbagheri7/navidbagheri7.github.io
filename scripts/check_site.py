"""Validate the static website's navigation, local assets and publication metadata."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://navidbagheri7.github.io/'
PAGES = ['index.html', 'publications.html', 'academic.html', 'repositories.html', 'contact.html']

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs, self.meta, self.canonicals = set(), [], {}, []
        self.titles = self.headings = self.current = 0
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            assert a['id'] not in self.ids, 'Duplicate ID: '+a['id']
            self.ids.add(a['id'])
        self.titles += tag == 'title'
        self.headings += tag == 'h1'
        self.current += a.get('aria-current') == 'page'
        if tag == 'meta':
            self.meta[a.get('name') or a.get('property')] = a.get('content')
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonicals.append(a['href'])
        if tag in ['a', 'link'] and 'href' in a:
            self.refs.append(a['href'])
        if tag in ['img', 'script'] and 'src' in a:
            self.refs.append(a['src'])
        if tag == 'img':
            assert a.get('alt'), 'Image needs alternative text'
        if tag == 'a' and a.get('target') == '_blank':
            assert {'noopener', 'noreferrer'} <= set(a.get('rel','').split())


def main():
    documents = {name: Document((ROOT/name).read_text()) for name in PAGES}
    count = 0
    for name, d in documents.items():
        assert (d.titles,d.headings,d.current) == (1,1,1), name
        expected = BASE + ('' if name == 'index.html' else name)
        assert d.canonicals == [expected] and d.meta['og:url'] == expected
        assert d.meta['description'] and d.meta['og:title'] and d.meta['og:image']
        for ref in d.refs:
            u = urlsplit(ref)
            if u.scheme or u.netloc:
                assert u.scheme in ['https','mailto'], ref
                continue
            target = (ROOT/(unquote(u.path) or name)).resolve()
            assert target.is_relative_to(ROOT) and target.is_file(), (name,ref)
            if u.fragment and target.name in documents:
                assert unquote(u.fragment) in documents[target.name].ids, (name,ref)
            count += 1
    for font in re.findall(r'url\([\'\"]?([^\)\'\"]+)', (ROOT/'styles.css').read_text()):
        assert (ROOT/font).is_file(), font
    repository_text = (ROOT/'repositories.html').read_text()
    for slug in ['learning-generalization-lab','certified-optimization-lab','sequential-decision-lab','diffusion-flow-lab','sampling-energy-lab','information-theory-lab']:
        assert 'https://github.com/navidbagheri7/'+slug in repository_text
        assert 'https://navidbagheri7.github.io/'+slug+'/' in repository_text
    assert (ROOT/'assets/navid-bagheri-shouraki-cv.pdf').read_bytes().startswith(b'%PDF-')
    assert (ROOT/'.nojekyll').exists()
    print(f'Validated {len(documents)} pages, {count} local references, font files and six lab links.')

if __name__ == '__main__':
    main()
