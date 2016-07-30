package au.gov.govhack.api

import au.gov.govhack.datasource.RealtimeAirQuality
import groovy.util.logging.Commons
import io.swagger.annotations.ApiParam
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.data.mongodb.core.MongoTemplate
import org.springframework.data.mongodb.core.query.Query
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

import static org.springframework.data.mongodb.core.query.Criteria.where
import static org.springframework.web.bind.annotation.RequestMethod.GET

@Commons
@RestController
class Monitoring {
    @Autowired
    MongoTemplate mongoTemplate

    @Autowired
    RealtimeAirQuality airQuality;

    @RequestMapping(value = "/api/monitoring", method = GET)
    ResponseEntity<List<String>> monitoringTypes() throws Exception {
        List<String> types = ['All', 'Air quality', 'Storm tide', 'Water quality', 'Wave height and direction']
        ResponseEntity.ok types
    }

    String rawQuery(String collection, Query query) {
        mongoTemplate.find(query, String, collection)
    }

    ResponseEntity<String> rawQueryResponse(String collection, Query query = null) {
        ResponseEntity.ok rawQuery(collection, query)
    }

    @RequestMapping(value = "/api/monitoring/{type}", method = GET, produces = "application/json")
    ResponseEntity<String> monitoringLocations(
            @ApiParam(value="Monitoring type", name="type", defaultValue = "All")
            @PathVariable('type') String type) throws Exception {

        rawQueryResponse 'monitoring_list',
                'all'.equalsIgnoreCase(type) ? new Query() : new Query(where('Monitor').is(type))
    }

    @RequestMapping(value = '/api/airquality/{category}', method = GET, produces = 'application/json')
    public ResponseEntity<String> realtimeAirQuality(
            @ApiParam(value='Air Quality Category', name='category', defaultValue='1')
            @PathVariable('category') int category) throws Exception {

        ResponseEntity.ok airQuality.getRealtimeData(category)
    }

    @RequestMapping(value = '/api/emissions/qld/fugitiveAir/{postcode}', method = GET, produces = 'application/json')
    public ResponseEntity<String> fugitiveAirEmissionsQld(
            @ApiParam(value='postcode', name='postcode', defaultValue='4413')
            @PathVariable('postcode') String postcode) throws Exception {

        rawQueryResponse 'npi_2015_qld_air_fugitive_emissions',
                new Query(where('site_address_postcode').is(postcode))
    }


    @RequestMapping(value = '/api/emissions/qld/pointAir/{postcode}', method = GET, produces = 'application/json')
    public ResponseEntity<String> pointAirEmissionsQld(
            @ApiParam(value='postcode', name='postcode', defaultValue='4871')
            @PathVariable('postcode') String postcode) throws Exception {

        rawQueryResponse 'npi_2015_qld_air_point_emissions',
                new Query(where('site_address_postcode').is(postcode))
    }


    @RequestMapping(value = '/api/emissions/qld/totalAir/{postcode}', method = GET, produces = 'application/json')
    public ResponseEntity<String> totalAirEmissionsQld(
            @ApiParam(value='postcode', name='postcode', defaultValue='4413')
            @PathVariable('postcode') String postcode) throws Exception {

        rawQueryResponse 'npi_2015_qld_air_total_emissions',
                new Query(where('site_address_postcode').is(postcode))
    }

    @RequestMapping(value = '/api/emissions/qld/land/{postcode}', method = GET, produces = 'application/json')
    public ResponseEntity<String> landEmissionsQld(
            @ApiParam(value='postcode', name='postcode', defaultValue='4303')
            @PathVariable('postcode') String postcode) throws Exception {

        rawQueryResponse 'npi_2015_qld_land_emissions',
                new Query(where('site_address_postcode').is(postcode))
    }

    @RequestMapping(value = '/api/emissions/qld/transfers/{postcode}', method = GET, produces = 'application/json')
    public ResponseEntity<String> transfersEmissionsQld(
            @ApiParam(value='postcode', name='postcode', defaultValue='4721')
            @PathVariable('postcode') String postcode) throws Exception {

        rawQueryResponse 'npi_2015_qld_transfers',
                new Query(where('site_address_postcode').is(postcode))
    }

    @RequestMapping(value = '/api/emissions/qld/water/{postcode}', method = GET, produces = 'application/json')
    public ResponseEntity<String> waterEmissionsQld(
            @ApiParam(value='postcode', name='postcode', defaultValue='4721')
            @PathVariable('postcode') String postcode) throws Exception {

        rawQueryResponse 'npi_2015_qld_water_emissions',
                new Query(where('site_address_postcode').is(postcode))
    }

}
