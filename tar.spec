Summary:	A GNU file archiving program
Summary(de):	GNU-Magnetband-Archivierprogramm (tar)
Summary(fr):	Programme d'archivage GNU (tar : GNU Tape Archiver).
Summary(pl):	Program do archiwizacji (GNU)
Summary(tr):	Yaygýn kullanýlan yedekleyici
Name:		tar
Version:	1.13.17
Release:	1
Epoch:		1
Copyright:	GPL
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
Source0:	ftp://alpha.gnu.org/gnu/tar/%{name}-%{version}.tar.gz
Source1:	tar.1.pl
Patch0:		tar-manpage.patch
Patch1:		tar-info.patch
Patch2:		tar-pipe.patch
Patch3:		tar-namecache.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_libexecdir	/sbin

%description
The GNU tar program saves many files together into one archive and can
restore individual files (or all of the files) from the archive. Tar can
also be used to add supplemental files to an archive and to update or list
files in the archive.

Tar includes multivolume support, automatic archive compression/
decompression, the ability to perform remote archives and the ability to
perform incremental and full backups.

If you want to use Tar for remote backups, you'll also need to install the
rmt package.

You should install the tar package, because you'll find its compression and
decompression utilities essential for working with files.

%description -l de
Das GNU tar-Programm speichert mehrere Dateien in ein Archiv, und kann
einzelne Dateien daraus wiederherstellen (oder auch alle Dateien). Tar kann
auch benutzt werden, um einem Archiv Dateien hinzuzufügen, und um die Liste
der Dateien im Archiv anzuzeigen oder zu verändern.

Tar enthält multivolume-Support, automatische
Archivkompression/dekompression, the Möglichkeit, Dateien per Netzwerk zu
archivieren und die Möglichkeit zu inkrementellen backups.

Wenn Sie tar für Netzwerkbackups benutzen wollen, brauchen Sie außerdem das
rmt-Paket.

Sie sollten tar installieren, da es wichtig zur Dateibehandlung ist.

%description -l fr
Le programme GNU tar permet de regrouper plusieurs fichiers en une seule
archive et d'effectuer diverses opérations sur cette archive (extraction
d'un fichier particulier, mise à jour, ajout d'un nouveau fichier, ...).

Tar gère les archives multi-volumes, la compression et la décompression de
manière transparente ainsi que la possibilité de réaliser des sauvegardes
incrémentales et des sauvegardes complètes.

Si vous comptez utiliser Tar pour des sauvegardes distantes, vous devriez
également installer le programme rmt.

Tar devrait être installé sur tout système car ses capacité de
(dé)compression sont essentielles pour travailler sur les fichiers.

Pour profiter pleinement de tar, vous devriez installer les compresseurs
gzip et/ou bzip2.

%description -l pl
Program GNU tar s³u¿y do zapisywania wielu plików w pojedynczym archiwum i
moze tak¿e s³u¿yæ do odzyskiwania z tak prepaowanych archiwów pojedynczych
plików (lub wszystkich). Za jego pomoc± mo¿na tak¿e dodwaæ nowe pliki do ju¿
istiej±cego archiwum.

GNU tar umo¿liwia robienie wieloczê¶ciowych archiwów (multivolume archive),
automatyczn± kompresjê i dekompresjê samego archiwum a tak¿e ma mo¿liwo¶æ
operowania na zdalnych archiiwach co jest przydatne przy sporz±dzaniu
przyrostowych i pe³nych archiwów zasobów.

Je¿eli zamierzasz u¿ywaæ rprogramu tar do operowania na zdalnych archiwach
powiniene¶ doinstalowaæ pakiet rmt.

GNU tar s³u¿y do zapisywania wielu plików na ta¶mê lub dysk. Mo¿e odtwarzaæ
pojedyñcze pliki z archiwum. Umo¿liwia zapis du¿ego archiwum z podzia³em na
wiele no¶ników. Tar obs³uguje tak¿e automatyczn± kompresjê/dekompresjê i
archiwa zdalne. Posiada specjalne opcje do robienia pe³nych i przyrostowych
kopii bezpieczeñstwa. Aby tworzyæ zdalne archiwa tar-a trzeba zainstalowaæ
pakiet rmt.

%description -l tr
GNU tar, birden çok dosyayý tek bir manyetik bant ya da disk üzerinde
arþivleyebildiði gibi, bu dosyalarýn arþivden tek tek geri yüklenmesine de
izin verir. Çok kýsýmlý arþivleri, otomatik arþiv sýkýþtýrma ve açmayý, uzak
arþivleri, artýmsal yedeklemeyi destekler.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
chmod -R a+rwX .
gettextize --copy --force
LIBS="-lbsd" ; export LIBS
LDFLAGS="-s" ; export LDFLAGS
%configure

(cd doc; cp stamp-vti version.texi; touch *; makeinfo --force tar.texi)
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/bin,%{_mandir}/man1,%{_mandir}/pl/man1}

make DESTDIR=$RPM_BUILD_ROOT install

ln -s %{_bindir}/tar $RPM_BUILD_ROOT/usr/bin/gtar
install tar.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/tar.info*,%{_mandir}/man1/*} \
	$RPM_BUILD_ROOT%{_mandir}/*/man1/* \
	README NEWS

%find_lang %{name}

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(0644,root,root, 0755)
%doc NEWS.gz README.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /usr/bin/*
%{_infodir}/tar.info*
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
