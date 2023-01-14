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
         <ns1:bugs xsi:type="soapenc:Array" soapenc:arrayType="xsd:int[8]">
            <ns1:bugs xsi:type="xsd:int">753</ns1:bugs>
            <ns1:bugs xsi:type="xsd:int">837</ns1:bugs>
            <ns1:bugs xsi:type="xsd:int">841</ns1:bugs>
            <ns1:bugs xsi:type="xsd:int">843</ns1:bugs>
            <ns1:bugs xsi:type="xsd:int">844</ns1:bugs>
            <ns1:bugs xsi:type="xsd:int">865</ns1:bugs>
            <ns1:bugs xsi:type="xsd:int">895</ns1:bugs>
            <ns1:bugs xsi:type="xsd:int">952</ns1:bugs>
         </ns1:bugs>
      </ns1:get_status>
   </soap:Body>
</soap:Envelope>
"""

if __name__ == '__main__':
    template = jinja_env.from_string(xml)
    request_body = template.render({
        'queries': ['package', 'emacs', 'severity', 'normal', 'severity', 'important', 'severity', 'serious']
    })
    print(request_body)

    res = requests.post(
        'https://debbugs.gnu.org/cgi/soap.cgi',
        data=request_body,
        headers={
            'Content-Type': 'text/xml; charset=utf-8',
            'SOAPAction': 'SOAPAction: Debbugs/SOAP',
        },
    )
    print(res.text)
