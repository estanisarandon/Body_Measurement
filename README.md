# Projektuppgift Big Data

Ni kommer att få två dataset som anger olike kroppsmått för ett antal kvinnor, respektive män, samt en pdf-fil som dokumenterar datasetten.
Er uppgift är att skapa en applikation som underlättar inköp av kläder.
Utifrån måtten som återfinns i datasetten skall ni bestämma vilken klädesstorlek som de olika personerna i datasetten har. Gör det åtminstone för t-shirts. Användaren av ditt program skall ange sin längd och vikt och ditt program skall sedan utifrån datasetten bestämma vilken storlek på det aktuella klädesplagget som användaren bör ha.

### För G
- Bearbeta datasetten så att ni väljer ut ett antal kroppsmått som ni vill använda för att förutsäga varje persons storlek på det aktuella plagget
- Skriv de nya värdena till en eller flera csv-filer
- Skriv ett program som låter användaren ange sin längd och vikt
- Med hjälp av algortimen k-nearest neighbors, den angivna längden och vikten samt datat i datasetten du producerat skall du sedan beräkna vilken storlek på det aktuella plagget som programmet uppskattar att användaren skall ha
- Du skall själv skriva implementationen för k-nearest neighbors
  
**OBS**
- Du får själv hitta storlekstabeller online för det aktuella plagget
- För G krävs endast ett klädesplagg kunna behandlas

### FÖR VG
- Allt under G
- Ditt program skall kunna beräkna storlek för mer än ett plagg
- Ett av plaggen skall vara av en typ som har olika storleksberäkningar för män och kvinnor. Användaren skall, när mått för detta plagg skall beräknas, även ange sitt kön
- Verifiera din implementation av k-nearest neighbors genom att också använda en implementation från något package, förslagsvis sklearn. Låt den implementationen och din egen implementation båda göra en storleksberäkning och rapportera tillbaka båda resultaten till användaren
- Försök att använda dig av en annan maskininlärningsalgoritm för att göra samma uppskattnings som du gjort med k-nearest neighbors. Om den ger ett annat resultat försök beskriva vad det kan bero på. Beskrivningen kan göras som en kommentar i koden
