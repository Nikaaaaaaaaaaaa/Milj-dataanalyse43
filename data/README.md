Describes the data directory and datasets

#Potensielle API-kjelder
- Google dataset search
- Statistisk sentralbyrå
- eea.europa //Net Greenhouse Gass Emmissions fra EEA
    https://www.eea.europa.eu/en/datahub/featured-data/statistical-data/datahubitem-view/d22b842a-53f7-4c63-aa94-74d5fa1f4d40?activeAccordion=1093723
- ssb //Forsurende gasser, forurensing, etc
    https://www.ssb.no/statbank/table/08941/tableViewLayout1/
- api.met.no
- open-meteo.com
    Denne virker potensiellt velldig bra...


/Mappe_del_1, Oppgave 2/
1. Hvilke åpne datakilder er identifisert som relevante for miljødata, og hva er kriteriene (f.eks. kildeautoritet, datakvalitet, tilgjengelighet, brukervennlighet osv.) for å vurdere deres pålitelighet og kvalitet?
    - Vi har valgt å bruke Openweathermap sin API for å samle inn miljø-data, samt historisk data.
    - For å vurdere deres pålitelighet og kvalitet har vi sett på hvilke kilder denne siden bruker for å samle sin informasjon. Videre har vi forsøkt å bruke real-time tester for å se om de samsvarer med områdene vi søker på i virkeligheten. Dette var videre lagt fram som et forslag av Professor Rouhani.
2. Hvilke teknikker (f.eks. håndtering av CSV-filer, JSON-data) er valgt å bruke for å lese inn dataene, og hvordan påvirker disse valgene datakvaliteten og prosessen videre?
    - API-ene fra Openweathermap bruker JSON format. 
    - Vi har valgt å bruke Visual Studio Code for å arbeide med jupyter-book teknologi
3. Dersom det er brukt API-er, hvilke spesifikke API-er er valgt å bruke, og hva er de viktigste dataene som kan hentes fra disse kildene?
    - API-er fra Openweathermap som omhandler trender innenfor hvordan været har endret seg over tiden. Dette ligger sterkt med tanke på økende temperatur og sterkere vindforhold.



#API-er //ser ut til å ikke fungere fra openweather på grunn av limited subscription
Climate forecast 30 days
https://openweathermap.org/api/forecast30
API:
https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lon}&appid={API key}

Statistical weather data API
https://openweathermap.org/api/statistics-api
API:
history.openweathermap.org/data/2.5/aggregated/year?lat={lat}&lon={lon}&appid={API key}

Accumilated parameters --Nika
https://openweathermap.org/api/accumulated-parameters
API:
http://history.openweathermap.org/data/2.5/history/accumulated_temperature?lat={lat}&lon={lon}&start={start}&end={end}&threshold={threshold}&appid={API key}

History API -- Nika //kan ikke bruke fra openweather uten subscription
https://openweathermap.org/history
API:
https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&start={start}&end={end}&appid={API key}
>>>>>>> d981062e5e485670cf181fb340fbb5ad15ded938

/Mappe_Del_1, Oppgave 3/

1. For å kunne finne manglende verdier så vil dette kunne løses primært sett på to måter Først gjør en en test for å se om det finnes mangler. Om det mangler for mange verdier, så fjerner vi dem. Alternativt så kan vi fylle den inn selv, via flere forskjeller metoder. Eksempeltvis kan en gjøre det via en enkel count funksjon, alternativt ved å finne median-verdiene for de verdiene som mangler, basert på hva som er før og etter. 

2. Et eksempel som gitt over kan være via grafer. Når en først finner en mangel, så vil det umiddelbart være tre muligheter. De vil så være basert på fillna, hvor en har en forward fill som gir deg samme verdi som den siste nevnte før det var mangel. Den andre versjonen er en backwards fill hvor den så går til neste tall som blir git og fyller den inn baklengs. Den tredje versjonen er median fill, hvor en bruker en tar median-verdi for av hva som kommer etter og før de manglende verdiene for å gi en overgang.

3. Ved større datasett så vil Pandas SQL sørge for en mer nøyaktig framstilling for videre analyse.

4. I denne oppgaven planlegges det å møte manglende verdier, hvorav målet vil være å kunne finne ut hvor mange verdier som mangler av det totale datasettet. Om det skulle være for mange verdier, så vil disse droppes for å kunne unngå unøyaktigheter. Er de en påpasselig mengde, så vil vi gjøre en median-fill for å kunne sørge for en så gjennsnittlig måling som mulig. 
