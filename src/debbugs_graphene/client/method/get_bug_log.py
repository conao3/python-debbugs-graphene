from typing import Any
import xml.etree.ElementTree as ET

import jinja2
import requests

from ... import types


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
<ns1:get_bug_log>
<ns1:bugnumber xsi:type="xsd:int">952</ns1:bugnumber>
</ns1:get_bug_log>
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

    with open('tmp.conao3/get_bug_log__res.xml', mode='r') as f:
        res_text = f.read()

    root = ET.fromstring(res_text)
    ns = {
        'soap': "http://schemas.xmlsoap.org/soap/envelope/",
        'soapenc': "http://schemas.xmlsoap.org/soap/encoding/",
        'xsd': "http://www.w3.org/2001/XMLSchema",
        'xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'urn': "urn:Debbugs/SOAP",
    }
    items_array_tree = root.find('./soap:Body/urn:get_bug_logResponse/soapenc:Array', ns)
    assert items_array_tree is not None

    known_fields = {
        '{urn:Debbugs/SOAP}msg_num': ('msg_num', None),
        '{urn:Debbugs/SOAP}header': ('header', None),
        '{urn:Debbugs/SOAP}body': ('body', None),
        '{urn:Debbugs/SOAP}attachments': ('attachments', None),
    }

    items_tree = list(items_array_tree)
    for item_tree in items_tree:
        item_ = {}
        for elm in item_tree:
            if elm.tag in known_fields:
                mapping_key, fn = known_fields[elm.tag]
                item_[mapping_key] = fn(elm) if fn else elm.text

        print(types.BugLog.parse_obj(item_))
