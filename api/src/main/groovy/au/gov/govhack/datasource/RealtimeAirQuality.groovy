package au.gov.govhack.datasource

import org.json.JSONObject
import org.json.XML
import org.springframework.stereotype.Service

@Service
class RealtimeAirQuality {

    static String RESOURCE_URL = 'http://www.ehp.qld.gov.au/cgi-bin/air/xml.php?region=ALL';

    public String getRealtimeData(int category) {
        int textIndent = 2
        JSONObject xmlJSONObj = XML.toJSONObject(new URL("${RESOURCE_URL}&category=$category").text)
        xmlJSONObj.toString(textIndent)
    }

}
