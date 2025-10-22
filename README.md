# Tools
Za majhne aplikacije, ki jih pogosto uporabljam. Zastonj za svet

# Pdfjanje
v datoteki `merge_pdfs.py` se nahaja program ki združi več pdfjev v mapi. 
Navodila: 
1. Za program je potrebno imeti python in knjižnjico `PyPDF2` (`pip install PyPDF2`)
2. Program te vpraša po poti do mape kjer so shranjeni pdfji za združit. Naj bo pot podana v obliki `C:\neki\neki_drucga\itd\` (in ne v `"C:\\blablabla\\krneki\\itd\\"`)
3. *Vrsti red datotek ki jih bo program dal skupaj je urejen po abecedi*
4. Končna pot datoteke bo v mapi v kateri leži mapa s pdfji

# Označevalec slik
Ali si downloaal slike iz google photos (ali kje drugje) in bi jih zdaj rad uredil na računalniku? Brez skrbi! Ta prijezni program pikaže sliko in te vpraša, v katero mapo bi ga rad dal. Ko vpišeš `ntag`, te vpraša po imenu novega tega. To bo ustvarilo novo mapo v mapi map (glej `mapa_map` v kodi na vrhu in vstavi notri željeno pot) z istim imenom kot `ntag`. Ko vam program pokaže sliko, vi lahko vpišete ime tega ntaga in slika se bo prestavila v ciljno mapo. Če napišete le del besede, bo program dal v tisti ntag, ki vsebuje vpisan niz, če je tak ntag samo en, drugače pa ti napiše možnosti.

Če kej ne razumete vprašite.
