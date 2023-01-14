import xml.etree.ElementTree as ET

import jinja2
import requests


jinja_env = jinja2.Environment(autoescape=True)

xml = """\
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope
    soapenc:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:ns3="urn:Debbugs/SOAP/TYPES"
    xmlns:ns1="urn:Debbugs/SOAP"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
>
    <soap:Body>
        <ns1:get_bugs>
            <ns1:query xsi:type="soapenc:Array" soapenc:arrayType="xsd:anyType[{{ queries | length }}]">
                {%- for q in queries %}
                <ns1:query xsi:type="xsd:string">{{ q }}</ns1:query>
                {%- endfor %}
            </ns1:query>
        </ns1:get_bugs>
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

    with open('tmp.conao3/get_bugs__res.xml', mode='r') as f:
        res_text = f.read()

    root = ET.fromstring(res_text)
    ns = {
        'soap': "http://schemas.xmlsoap.org/soap/envelope/",
        'soapenc': "http://schemas.xmlsoap.org/soap/encoding/",
        'xsd': "http://www.w3.org/2001/XMLSchema",
        'xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'urn': "urn:Debbugs/SOAP",
    }
    items_array_tree = root.find('./soap:Body/urn:get_bugsResponse/soapenc:Array', ns)
    assert items_array_tree is not None

    items_tree = list(items_array_tree)
    items = [elm.text for elm in items_tree]
