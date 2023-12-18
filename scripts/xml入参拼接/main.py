

import re


if __name__ == "__main__":


    request = """<PatientId>210122652000</PatientId>
<VisitId>1</VisitId>
<PatientSource>2</PatientSource>
<OrgCode>H0001</OrgCode>
<Name>李关良</Name>
<ReportFlow>1.2.826.0.1.3680043.2.377.114.21.20221208131825299.520893</ReportFlow>
<ReportClassBelong>D</ReportClassBelong>
<ReportClass>EC</ReportClass>
<ReportName>床边心电图（18导）</ReportName>
<PublishDate>20231208133713</PublishDate>
<ValidDateTimeFrom>20231208133713</ValidDateTimeFrom>
<PageOrention>H</PageOrention>
<PageSize>A4</PageSize>
<PageCount>1</PageCount>
<PublishSystem>ECG</PublishSystem>
<PerformedBy>201131700</PerformedBy>
<ApplyFlow>01D2023120802395</ApplyFlow>
<Memo>备注</Memo>
<ImageFlow>1</ImageFlow>
<PrintPlace>门诊楼三楼</PrintPlace>
<PrintFlag>0</PrintFlag>
<UpdateFlag>1</UpdateFlag>"""
    for row in request.split("\n"):
        result1 = re.findall("<(.*)>.*</.*>", row)
        result2 = re.findall("<.*>(.*)</.*>", row)
        if len(result1) > 0 and len(result2) > 0:
            print(f'requestBody.append("<{result1[0]}>").append(param).append("</{result1[0]}>");')


