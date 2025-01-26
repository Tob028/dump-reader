pro jeden log partition (zhruba 32 kilo bajtu):
- prvni dva bajty: log next (adresa kam se bude zapisovat dalsi log)
- treti az tricatej patej bajt: prvni log entry
- tricatej sestej az tricatej osmej bajt: druhy log entry
- …

POZOR, neni zaruceno ze adresou v log next jsou validni logy (muze to bejt nejakej bordel kterej se jeste nenastavil, napriklad kdyz se zapsal jenom jeden log, tak neni zaruceny co je tam ulozeny, bohuzel neni jak zjistit jestli to co tam je, je validni - protoze se pri zapisovani doslo na konec alokovany adresi pro ten danej partition, nebo ne. je ale velka pravdepodobnost, ze pokud neni validni tak tak se tam budou nachazet samy 0xFF (1111 1111) )

pro jeden log entry (32 bajtu):
- prvni 4 bajty: timestamp (pocet sekund od nejakyho zacatku)
- patej bajt: flag
- sestej az tricatej druhej bajt: data

pokud flag == 255 and muj timestamp a timestamp predchoziho jsou dost blozko -> moje data patrej predchozimu log entry (data predchoziho se nevesly)