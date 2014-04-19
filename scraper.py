import scraperwiki
html = scraperwiki.scrape("https://www.secom.planalto.gov.br/consea/boletins.nsf/01ContatoxNome?OpenView&Start=1")
print html

import lxml.html
root = lxml.html.fromstring(html)
for table in root.cssselect('table'):
    td=table.cssselect ('tr td')
    if len(td)>5:
        data={
        'email': td[2].text_content(),
    }
print data

scraperwiki.sql.save(unique_keys=['email'], data=data)
