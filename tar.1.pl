.\" {PTM/LK/0.1/23-01-1999/"program archiwizuj�cy tar"}
.\" T�umaczenie: 23-01-1999 �ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
.\" @(#)tar.1 1.11.1 93/19/22 PJV;
.TH TAR 1 "22 Wrze�nia 1993"
.SH NAZWA
tar \- Wersja GNU Programu archiwizuj�cego tar
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
Ta strona opisuje wersj� GNU programu
.BR tar ","
kt�ry s�u�y do zapisywania i ekstrakcji plik�w z archiwum nazywanego
.IR tarfile.
Archiwum 
.IR tarfile 
mo�e zosta� utworzone w nap�dzie ta�my, chocia� cz�sto tworzy si� je w
postaci zwyk�ego pliku.
Pierwszym argumentem programu
.B tar
musi by� jedna z opcji
.BR Acdrtux ,
po kt�rej nast�puj� opcjonalne funkcje.
Ko�cowymi argumentami programu
.B tar
s� nazwy plik�w lub katalog�w, kt�re powinny zosta� zarchiwizowane. U�ycie
nazwy katalogu oznacza, �e znajduj�ce si� w nim podkatalogi r�wnie� powinny
zosta� zarchiwizowane.
.SH "FUNKCJE"
.TP
.B Zawsze nale�y u�y� jednej z nast�puj�cych opcji:
.TP
.B -A, --catenate, --concatenate
do��czenie istniej�cych plik�w .tar do archiwum
.TP
.B -c, --create	
utworzenie nowego archiwum
.TP
.B -d, --diff, --compare
znalezienie r�nic mi�dzy archiwum, a systemem plik�w
.TP
.B --delete		
usuni�cie plik�w z archiwum (opcji nie mo�na u�y� na ta�mach mag!)
.TP
.B -r, --append		
do��czenie plik�w do archiwum
.TP
.B -t, --list		
wypisanie zawarto�ci archiwum
.TP
.B -u, --update		
do��czenie tylko tych plik�w, kt�re s� nowsze ni� egzemplarze w archiwum
.TP
.B -x, --extract, --get		
ekstrakcja plik�w z archiwum
.SH "INNE OPCJE"
.TP
.B --atime-preserve	
pozostawienie oryginalnego czasu ostatniego dost�pu na dearchiwizowanych plikach
.TP
.B -b, --block-size N	
rozmiar bloku ma by� r�wny Nx512 bajt�w (domy�lnie N=20)
.TP
.B -B, --read-full-blocks	
zmieniaj rozmiar bloku podczas czytania archiwum (do u�ywania z nazwanymi
potokami 4.2BSD)
.TP 
.B -C, --directory DIR	
zmie� katalog na DIR
.TP 
.B --checkpoint		
wypisuj nazwy katalog�w w miar� czytania archiwum
.TP
.B -f, --file [HOSTNAME:]F
u�yj podanego pliku z archiwum lub urz�dzenia F (domy�lnie /dev/rmt0)
.TP
.B --force-local
plik z archiwum jest lokalny nawet, je�eli w jego nazwie wyst�puje dwukropek
.TP 
.B -F, --info-script F --new-volume-script F 
na ko�cu ka�dej ta�my uruchom podany skrypt (implikuje funkcjonalno�� opcji \-M)
.TP
.B -G, --incremental	
utw�rz/wypisz zawarto��/dearchiwizuj archiwum przyrostowe w starym formacie
GNU
.TP
.B -g, --listed-incremental F 
utw�rz/wypisz zawarto��/dearchiwizuj archiwum przyrostowe w nowym formacie
GNU
.TP 
.B -h, --dereference	
nie archiwizuj dowi�za� symbolicznych, tylko pliki, na kt�re one wskazuj�
.TP
.B -i, --ignore-zeros	
ignoruj bloki zawieraj�ce same zera (normalnie taki blok w archiwum oznacza
koniec pliku)
.TP
.B --ignore-failed-read	
nie ko�cz dzia�ania programu z niezerowym kodem wyj�cia po napotkaniu
plik�w, kt�re nie daj� si� odczyta�
.TP
.B -k, --keep-old-files	
ochrona istniej�cych plik�w; nie b�d� nadpisywane plikami z archiwum
.TP
.B -K, --starting-file F	
zacznij ekstrakcj� z archiwum od pliku F
.TP
.B -l, --one-file-system	
archiwizuj pliki tylko z bie��cego systemu plik�w
.TP
.B -L, --tape-length N	
zmiana ta�my po zapisaniu N*1024 bajt�w
.TP
.B -m, --modification-time	
nie dearchiwizuj czasu modyfikacji plik�w
.TP
.B -M, --multi-volume	
utw�rz/wypisz zawarto��/dearchiwizuj archiwum wielocz�ciowe
.TP
.B -N, --after-date DATA, --newer DATA
archiwizuj wy��cznie pliki nowsze, ni� DATA
.TP
.B -o, --old-archive, --portability	
zapisz archiwum w formacie V7, nie ANSI
.TP
.B -O, --to-stdout		
dearchiwizuj pliki na standardowe wyj�cie
.TP
.B -p, --same-permissions, --preserve-permissions 
dearchiwizuj wszystkie informacje o prawach dost�pu
.TP
.B -P, --absolute-paths	
nie usuwaj z nazw plik�w wiod�cych znak�w '/'
.TP
.B --preserve		
takie samo dzia�anie, jak opcje \-p \-s
.TP
.B -R, --record-number	
przy ka�dej wiadomo�ci pokazuj numer rekordu wewn�trz archiwum
.TP 
.B --remove-files		
usuwaj pliki po dodaniu ich do archiwum
.TP
.B -s, --same-order, --preserve-order	
lista nazw plik�w do dearchiwizacji jest sortowana, by pasowa� do archiwum
.TP
.B --same-owner		
zachowanie nazwy w�a�ciciela pliku zgodnie z zachowan� w archiwum
.TP
.B -S, --sparse		
efektywna obs�uga plik�w rozsianych po archiwach
.\"handle sparse files efficiently
.TP 
.B -T, --files-from F	
nazwy plik�w do dearchiwizacji s� pobierane z pliku F
.TP
.B --null			
opcja -T odczytuje nazwy plik�w zako�czone znakiem '\\0', opcja -C w�wczas nie
dzia�a
.TP
.B --totals		
zapisz ca�kowit� liczb� bajt�w zapisanych przez --create
.TP
.B -v, --verbose		
wypisywanie nazw wszystkich plik�w
.TP
.B -V, --label NAZWA
utworzenie archiwum z woluminem o nazwie NAZWA
.TP 
.B --version		
wypisanie numeru wersji programu 
.B tar
.TP
.B -w, --interactive, --confirmation	
pytanie o zgod� na ka�de dzia�anie
.TP
.B -W, --verify		
weryfikacja archiwum po jego utworzeniu
.TP
.B --exclude PLIK
wy��czenie z archiwizacji pliku PLIK
.TP
.B -X, --exclude-from PLIK
wy��czenie z archiwizacji plik�w o nazwach wymienionych w pliku PLIK
.TP
.B -Z, --compress, --uncompress      	
skompresowanie archimum programem compress
.TP 
.B -z, --gzip, --ungzip		
skompresowanie archiwum programem gzip
.TP
.B --use-compress-program PROG
skompresowanie archiwum programem PROG (kt�ry musi akceptowa� opcj� -d
oznaczaj�c� dekompresj�)
.TP
.B --block-compress	
dzielenie skompresowanego archiwum dla ta�m
.TP
.B -[0-7][lmh]		
okre�lenie nap�du i g�sto�ci
