import jinja2

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
    template = jinja_env.from_string(xml)
    print(
        template.render({
            'queries': ['package', 'emacs', 'severity', 'normal', 'severity', 'important', 'severity', 'serious']
        })
    )
