.\" {PTM/LK/0.1/23-01-1999/"program archiwizuj±cy tar"}
.\" T³umaczenie: 23-01-1999 £ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
.\" @(#)tar.1 1.11.1 93/19/22 PJV;
.TH TAR 1 "22 Wrze¶nia 1993"
.SH NAZWA
tar \- Wersja GNU Programu archiwizuj±cego tar
.SH STRESZCZENIE
.B tar
[
.B \-
]
.B A --catenate --concatenate \||\| c --create \||\| d --diff --compare \||\| r --append \||\| t --list \||\| u --update \||\| x -extract --get
[
.B --atime-preserve
]
[
.B -b, --block-size N
]
[
.B -B, --read-full-blocks
]
[
.B -C, --directory DIR
]
[
.B --checkpoint	
]
[
.B -f, --file [HOSTNAME:]F
]
[
.B --force-local	
]
[
.B -F, --info-script F --new-volume-script F
]
[
.B -G, --incremental
]
[
.B -g, --listed-incremental F
]
[
.B -h, --dereference
]
[
.B -i, --ignore-zeros
]
[
.B --ignore-failed-read
]
[
.B -k, --keep-old-files
]
[
.B -K, --starting-file F
]
[
.B -l, --one-file-system
]
[
.B -L, --tape-length N
]
[
.B -m, --modification-time
]
[
.B -M, --multi-volume
]
[
.B -N, --after-date DATA, --newer DATA
]
[
.B -o, --old-archive, --portability
]
[
.B -O, --to-stdout
]
[
.B -p, --same-permissions, --preserve-permissions
]
[
.B -P, --absolute-paths
]
[
.B --preserve	
]
[
.B -R, --record-number
]
[
.B --remove-files
]
[
.B -s, --same-order, --preserve-order
]
[
.B --same-owner
]
[
.B -S, --sparse
]
[
.B -T, --files-from F
]
[
.B --null	
]
[
.B --totals	
]
[
.B -v, --verbose
]
[
.B -V, --label NAZWA
]
[
.B --version	
]
[
.B -w, --interactive, --confirmation
]
[
.B -W, --verify	
]
[
.B --exclude PLIK
]
[
.B -X, --exclude-from PLIK
]
[
.B -Z, --compress, --uncompress
]
[
.B -z, --gzip, --ungzip	
]
[
.B --use-compress-program PROG
]
[
.B --block-compress
]
[
.B -[0-7][lmh]	
]
.TP
.I plik1 [ plik2, ... plikN ] 
.TP
.I katalog1 [ katalog2, ...katalogN ]
.SH OPIS
.LP
Ta strona opisuje wersjê GNU programu
.BR tar ","
który s³u¿y do zapisywania i ekstrakcji plików z archiwum nazywanego
.IR tarfile.
Archiwum 
.IR tarfile 
mo¿e zostaæ utworzone w napêdzie ta¶my, chocia¿ czêsto tworzy siê je w
postaci zwyk³ego pliku.
Pierwszym argumentem programu
.B tar
musi byæ jedna z opcji
.BR Acdrtux ,
po której nastêpuj± opcjonalne funkcje.
Koñcowymi argumentami programu
.B tar
s± nazwy plików lub katalogów, które powinny zostaæ zarchiwizowane. U¿ycie
nazwy katalogu oznacza, ¿e znajduj±ce siê w nim podkatalogi równie¿ powinny
zostaæ zarchiwizowane.
.SH "FUNKCJE"
.TP
.B Zawsze nale¿y u¿yæ jednej z nastêpuj±cych opcji:
.TP
.B -A, --catenate, --concatenate
do³±czenie istniej±cych plików .tar do archiwum
.TP
.B -c, --create	
utworzenie nowego archiwum
.TP
.B -d, --diff, --compare
znalezienie ró¿nic miêdzy archiwum, a systemem plików
.TP
.B --delete		
usuniêcie plików z archiwum (opcji nie mo¿na u¿yæ na ta¶mach mag!)
.TP
.B -r, --append		
do³±czenie plików do archiwum
.TP
.B -t, --list		
wypisanie zawarto¶ci archiwum
.TP
.B -u, --update		
do³±czenie tylko tych plików, które s± nowsze ni¿ egzemplarze w archiwum
.TP
.B -x, --extract, --get		
ekstrakcja plików z archiwum
.SH "INNE OPCJE"
.TP
.B --atime-preserve	
pozostawienie oryginalnego czasu ostatniego dostêpu na dearchiwizowanych plikach
.TP
.B -b, --block-size N	
rozmiar bloku ma byæ równy Nx512 bajtów (domy¶lnie N=20)
.TP
.B -B, --read-full-blocks	
zmieniaj rozmiar bloku podczas czytania archiwum (do u¿ywania z nazwanymi
potokami 4.2BSD)
.TP 
.B -C, --directory DIR	
zmieñ katalog na DIR
.TP 
.B --checkpoint		
wypisuj nazwy katalogów w miarê czytania archiwum
.TP
.B -f, --file [HOSTNAME:]F
u¿yj podanego pliku z archiwum lub urz±dzenia F (domy¶lnie /dev/rmt0)
.TP
.B --force-local
plik z archiwum jest lokalny nawet, je¿eli w jego nazwie wystêpuje dwukropek
.TP 
.B -F, --info-script F --new-volume-script F 
na koñcu ka¿dej ta¶my uruchom podany skrypt (implikuje funkcjonalno¶æ opcji \-M)
.TP
.B -G, --incremental	
utwórz/wypisz zawarto¶æ/dearchiwizuj archiwum przyrostowe w starym formacie
GNU
.TP
.B -g, --listed-incremental F 
utwórz/wypisz zawarto¶æ/dearchiwizuj archiwum przyrostowe w nowym formacie
GNU
.TP 
.B -h, --dereference	
nie archiwizuj dowi±zañ symbolicznych, tylko pliki, na które one wskazuj±
.TP
.B -i, --ignore-zeros	
ignoruj bloki zawieraj±ce same zera (normalnie taki blok w archiwum oznacza
koniec pliku)
.TP
.B --ignore-failed-read	
nie koñcz dzia³ania programu z niezerowym kodem wyj¶cia po napotkaniu
plików, które nie daj± siê odczytaæ
.TP
.B -k, --keep-old-files	
ochrona istniej±cych plików; nie bêd± nadpisywane plikami z archiwum
.TP
.B -K, --starting-file F	
zacznij ekstrakcjê z archiwum od pliku F
.TP
.B -l, --one-file-system	
archiwizuj pliki tylko z bie¿±cego systemu plików
.TP
.B -L, --tape-length N	
zmiana ta¶my po zapisaniu N*1024 bajtów
.TP
.B -m, --modification-time	
nie dearchiwizuj czasu modyfikacji plików
.TP
.B -M, --multi-volume	
utwórz/wypisz zawarto¶æ/dearchiwizuj archiwum wieloczê¶ciowe
.TP
.B -N, --after-date DATA, --newer DATA
archiwizuj wy³±cznie pliki nowsze, ni¿ DATA
.TP
.B -o, --old-archive, --portability	
zapisz archiwum w formacie V7, nie ANSI
.TP
.B -O, --to-stdout		
dearchiwizuj pliki na standardowe wyj¶cie
.TP
.B -p, --same-permissions, --preserve-permissions 
dearchiwizuj wszystkie informacje o prawach dostêpu
.TP
.B -P, --absolute-paths	
nie usuwaj z nazw plików wiod±cych znaków '/'
.TP
.B --preserve		
takie samo dzia³anie, jak opcje \-p \-s
.TP
.B -R, --record-number	
przy ka¿dej wiadomo¶ci pokazuj numer rekordu wewn±trz archiwum
.TP 
.B --remove-files		
usuwaj pliki po dodaniu ich do archiwum
.TP
.B -s, --same-order, --preserve-order	
lista nazw plików do dearchiwizacji jest sortowana, by pasowaæ do archiwum
.TP
.B --same-owner		
zachowanie nazwy w³a¶ciciela pliku zgodnie z zachowan± w archiwum
.TP
.B -S, --sparse		
efektywna obs³uga plików rozsianych po archiwach
.\"handle sparse files efficiently
.TP 
.B -T, --files-from F	
nazwy plików do dearchiwizacji s± pobierane z pliku F
.TP
.B --null			
opcja -T odczytuje nazwy plików zakoñczone znakiem '\\0', opcja -C wówczas nie
dzia³a
.TP
.B --totals		
zapisz ca³kowit± liczbê bajtów zapisanych przez --create
.TP
.B -v, --verbose		
wypisywanie nazw wszystkich plików
.TP
.B -V, --label NAZWA
utworzenie archiwum z woluminem o nazwie NAZWA
.TP 
.B --version		
wypisanie numeru wersji programu 
.B tar
.TP
.B -w, --interactive, --confirmation	
pytanie o zgodê na ka¿de dzia³anie
.TP
.B -W, --verify		
weryfikacja archiwum po jego utworzeniu
.TP
.B --exclude PLIK
wy³±czenie z archiwizacji pliku PLIK
.TP
.B -X, --exclude-from PLIK
wy³±czenie z archiwizacji plików o nazwach wymienionych w pliku PLIK
.TP
.B -Z, --compress, --uncompress      	
skompresowanie archimum programem compress
.TP 
.B -z, --gzip, --ungzip		
skompresowanie archiwum programem gzip
.TP
.B --use-compress-program PROG
skompresowanie archiwum programem PROG (który musi akceptowaæ opcjê -d
oznaczaj±c± dekompresjê)
.TP
.B --block-compress	
dzielenie skompresowanego archiwum dla ta¶m
.TP
.B -[0-7][lmh]		
okre¶lenie napêdu i gêsto¶ci
