import xml.etree.ElementTree as ET

import jinja2
import requests


jinja_env = jinja2.Environment(autoescape=True)

xml = """\
<soap:Envelope
    soapenc:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:ns1="urn:Debbugs/SOAP"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
>
    <soap:Body>
        <ns1:newest_bugs>
            <ns1:amount xsi:type="xsd:int">10</ns1:amount>
        </ns1:newest_bugs>
    </soap:Body>
</soap:Envelope>
"""

if __name__ == '__main__':
    # template = jinja_env.from_string(xml)
    # request_body = template.render({
    #     'queries': ['package', 'emacs', 'severity', 'normal', 'severity', 'important', 'severity', 'serious']
    # })
    # print(request_body)

    # res = requests.post(
    #     'https://debbugs.gnu.org/cgi/soap.cgi',
    #     data=request_body,
    #     headers={
    #         'Content-Type': 'text/xml; charset=utf-8',
    #         'SOAPAction': 'SOAPAction: Debbugs/SOAP',
    #     },
    # )
    # print(res.text)

    with open('tmp.conao3/get_newest_bugs__res.xml', mode='r') as f:
        res_text = f.read()

    root = ET.fromstring(res_text)
    ns = {
        'soap': "http://schemas.xmlsoap.org/soap/envelope/",
        'soapenc': "http://schemas.xmlsoap.org/soap/encoding/",
        'xsd': "http://www.w3.org/2001/XMLSchema",
        'xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'urn': "urn:Debbugs/SOAP",
    }
    items_array_tree = root.find('./soap:Body/urn:newest_bugsResponse/soapenc:Array', ns)
    assert items_array_tree is not None

    items_tree = list(items_array_tree)
    items = [int(elm.text) for elm in items_tree if elm.text is not None]
    print(items)
