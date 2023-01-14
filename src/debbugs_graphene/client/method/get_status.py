import xml.etree.ElementTree as ET

import jinja2
import requests


jinja_env = jinja2.Environment(autoescape=True)

xml = """\
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:ns1="urn:Debbugs/SOAP"
    xmlns:ns3="urn:Debbugs/SOAP/TYPES"
    xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    soapenc:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
>
    <soap:Body>
        <ns1:get_status>
            <ns1:bugs xsi:type="soapenc:Array" soapenc:arrayType="xsd:int[{{ bugs | length }}]">
                {%- for bug in bugs %}
                <ns1:bugs xsi:type="xsd:int">{{ bug }}</ns1:bugs>
                {%- endfor %}
            </ns1:bugs>
        </ns1:get_status>
    </soap:Body>
</soap:Envelope>
"""

if __name__ == '__main__':
    # template = jinja_env.from_string(xml)
    # request_body = template.render({
    #     'bugs': [753, 837, 841, 843, 844, 865, 895, 952]
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

    with open('tmp.conao3/get_status__res.xml', mode='r') as f:
        res_text = f.read()

    root = ET.fromstring(res_text)
    ns = {
        'soap': "http://schemas.xmlsoap.org/soap/envelope/",
        'apachens': "http://xml.apache.org/xml-soap",
        'soapenc': "http://schemas.xmlsoap.org/soap/encoding/",
        'xsd': "http://www.w3.org/2001/XMLSchema",
        'xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'urn': "urn:Debbugs/SOAP",
    }
    items_array_tree = root.find('soap:Body/urn:get_statusResponse/urn:s-gensym3', ns)
    assert items_array_tree is not None

    items_tree = list(items_array_tree)
    for item_tree in items_tree:
        key_tree = item_tree.find('urn:key', ns)
        assert key_tree is not None

        value_tree = item_tree.find('urn:value', ns)
        assert value_tree is not None

        print(key_tree.text)
