Summary:	A GNU file archiving program
Summary(de):	GNU-Magnetband-Archivierprogramm (tar)
Summary(fr):	Programme d'archivage GNU (tar : GNU Tape Archiver).
Summary(pl):	Program do archiwizacji (GNU)
Summary(tr):	Yayg�n kullan�lan yedekleyici
Name:		tar
Version:	1.13.17
Release:	1
Epoch:		1
Copyright:	GPL
Group:		Utilities/Archiving
Group(pl):	Narz�dzia/Archiwizacja
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
auch benutzt werden, um einem Archiv Dateien hinzuzuf�gen, und um die Liste
der Dateien im Archiv anzuzeigen oder zu ver�ndern.

Tar enth�lt multivolume-Support, automatische
Archivkompression/dekompression, the M�glichkeit, Dateien per Netzwerk zu
archivieren und die M�glichkeit zu inkrementellen backups.

Wenn Sie tar f�r Netzwerkbackups benutzen wollen, brauchen Sie au�erdem das
rmt-Paket.

Sie sollten tar installieren, da es wichtig zur Dateibehandlung ist.

%description -l fr
Le programme GNU tar permet de regrouper plusieurs fichiers en une seule
archive et d'effectuer diverses op�rations sur cette archive (extraction
d'un fichier particulier, mise � jour, ajout d'un nouveau fichier, ...).

Tar g�re les archives multi-volumes, la compression et la d�compression de
mani�re transparente ainsi que la possibilit� de r�aliser des sauvegardes
incr�mentales et des sauvegardes compl�tes.

Si vous comptez utiliser Tar pour des sauvegardes distantes, vous devriez
�galement installer le programme rmt.

Tar devrait �tre install� sur tout syst�me car ses capacit� de
(d�)compression sont essentielles pour travailler sur les fichiers.

Pour profiter pleinement de tar, vous devriez installer les compresseurs
gzip et/ou bzip2.

%description -l pl
Program GNU tar s�u�y do zapisywania wielu plik�w w pojedynczym archiwum i
moze tak�e s�u�y� do odzyskiwania z tak prepaowanych archiw�w pojedynczych
plik�w (lub wszystkich). Za jego pomoc� mo�na tak�e dodwa� nowe pliki do ju�
istiej�cego archiwum.

GNU tar umo�liwia robienie wielocz�ciowych archiw�w (multivolume archive),
automatyczn� kompresj� i dekompresj� samego archiwum a tak�e ma mo�liwo��
operowania na zdalnych archiiwach co jest przydatne przy sporz�dzaniu
przyrostowych i pe�nych archiw�w zasob�w.

Je�eli zamierzasz u�ywa� rprogramu tar do operowania na zdalnych archiwach
powiniene� doinstalowa� pakiet rmt.

GNU tar s�u�y do zapisywania wielu plik�w na ta�m� lub dysk. Mo�e odtwarza�
pojedy�cze pliki z archiwum. Umo�liwia zapis du�ego archiwum z podzia�em na
wiele no�nik�w. Tar obs�uguje tak�e automatyczn� kompresj�/dekompresj� i
archiwa zdalne. Posiada specjalne opcje do robienia pe�nych i przyrostowych
kopii bezpiecze�stwa. Aby tworzy� zdalne archiwa tar-a trzeba zainstalowa�
pakiet rmt.

%description -l tr
GNU tar, birden �ok dosyay� tek bir manyetik bant ya da disk �zerinde
ar�ivleyebildi�i gibi, bu dosyalar�n ar�ivden tek tek geri y�klenmesine de
izin verir. �ok k�s�ml� ar�ivleri, otomatik ar�iv s�k��t�rma ve a�may�, uzak
ar�ivleri, art�msal yedeklemeyi destekler.

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
