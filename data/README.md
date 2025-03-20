Describes the data directory and datasets

Net Greenhouse Gass Emmissions fra EEA
https://www.eea.europa.eu/en/datahub/featured-data/statistical-data/datahubitem-view/d22b842a-53f7-4c63-aa94-74d5fa1f4d40?activeAccordion=1093723

Forsurende gasser, forurensing, etc
https://www.ssb.no/statbank/table/08941/tableViewLayout1/

Google dataset search

Statistisk sentralbyrå

<<<<<<< HEAD
Vi har valgt å bruke Openweathermap sin API for å samle inn miljø-data, samt historisk data. Det viktigste informasjon over hvordan trender innenfor været har endret seg over tiden. Dette ligger sterkt med tanke på økende temperatur og sterkere vindforhold.
API brukt: https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lon}&appid={API_key}


For å vurdere deres pålitelighet og kvalitet har vi sett på hvilke kilder denne siden bruker for å samle sin informasjon. Videre har vi forsøkt å bruke real-time tester for å se om de samsvarer med områdene vi søker på i virkeligheten. Dette var videre lagt fram som et forslag av Professor Rouhani.
=======


#API-er
Climate forecast 30 days
https://openweathermap.org/api/forecast30
API:
https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lon}&appid={API key}

Statistical weather data API
https://openweathermap.org/api/statistics-api
API:
history.openweathermap.org/data/2.5/aggregated/year?lat={lat}&lon={lon}&appid={API key}

Accumilated parameters
https://openweathermap.org/api/accumulated-parameters
API:
http://history.openweathermap.org/data/2.5/history/accumulated_temperature?lat={lat}&lon={lon}&start={start}&end={end}&threshold={threshold}&appid={API key}

History API
https://openweathermap.org/history
API:
https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&start={start}&end={end}&appid={API key}
>>>>>>> d981062e5e485670cf181fb340fbb5ad15ded938
