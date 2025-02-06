# Autolainaus
Ohjelma on Rasekon auto-osaston autojen lainaamiseen tarkoitettu PySide6-sovellus. Autoja lainataan itsepalveluperiaatteella. Opiskelija ottaa auton käyttöön lukemalla henkilötunnusviivakoodin omasta ajokortistaan ja auton avaimenperässä olevasta viivakoodista auton rekisterinumeron. Sovelluksessa on tietokanta, jossa on lainaukseen oikeutettujen opiskelijoidet tiedot: Henkilötunnus, nimi ja ryhmä (luokka). Autosta tietoina ovat rekisteritunnus, merkki, malli ja vuosimalli. Tietokantaan rekisteröidään tieto auton lainauksesta: Päivämäärä, kellonaika, lainaajan henkilötunnus ja auton rekisterinumero. Palautuksesta kirjataan rekisteritunnus ja palautusaika. Sovelluksessa ainoastaan opettajalla on käytössään hiiri ja näppäimistö. Opiskelijat syöttävät tieot viivakoodinlukijan avulla. He voivat navigoida käyttöliittymässä ainoastaan kosketusnäytön avulla.

Lainaus-sivu sovelluksessa voisi näyttää esim. seuraavalta:

![image](https://github.com/user-attachments/assets/c173cac4-62d4-4068-9319-f612835d1d91)

Palautus-sivu taas voisi olla esim. seuraavan kalatainen:

![image](https://github.com/user-attachments/assets/56c9843b-fc1a-4f23-a4be-c1acd55a2486)

Opiskelija- ja ajoneuvotietojen syöttämiseen ja ajopäiväkirjojen katseluun tarvitaan myös sivut ne suunnitellaan perinteisinä lomakkeina.
Sovellus voidaan rakentaan yhtenä ohjelmana tai kahtena erillisenä ohjelmana, joista toisella ylläpidetään opiskelijoiden ja autojen tietoja sekä tulostetaan ajopäiväkirjatietoja ja toisella huolehditaan lainaus- ja palalautustapahtumien kirjaamisesta.

Projektiin liittyvät tehtävät ovat tämän repositorion **Issues**-välilehdellä.
