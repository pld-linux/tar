Summary:	GNU Tape Archiver (tar)
Summary(de):	GNU-Magnetband-Archivierprogramm (tar)
Summary(fr):	Programme d'archivage GNU (tar : GNU Tape Archiver).
Summary(pl):	Program do archiwizacji (GNU)
Summary(tr):	Yayg�n kullan�lan yedekleyici
Name:		tar
Version:	1.13
Release:	1
Copyright:	GPL
Group:		Utilities/Archiving
Group(pl):	Narz�dzia/Archiwizacja
Source0:	ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Source1:	tar-pl.po.patch
Source2:	tar.1.pl
Patch0:		tar-manpage.patch
Patch1:		tar-bzip2.patch
Patch2:		tar-cached_uid.patch
Patch3:		tar-bzip2-locale.patch
Patch4:		tar-info.patch
Patch5:		tar-pipe.patch
Patch6:		tar-namecache.patch
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

%define		_exec_prefix	/
%define		_libexecdir	/sbin

%description
GNU `tar' saves many files together into a single tape or disk archive, and
can restore individual files from the archive. It includes multivolume
support, the ability to archive sparse files, automatic archive
compression/decompression, remote archives and special features that allow
`tar' to be used for incremental and full backups. If you wish to do remote
backups with tar, you will need to install the `rmt' package as well.

%description -l de
GNU 'tar' speichert viele Dateien zusammen in ein einzelnes Band- oder
Disk-Archiv und kann einzelne Dateien aus dem Archiv wiederherstellen. Es
beinhaltet Multivolume-Support, die F�higkeit, seltene Dateien zu
archivieren, automatische Archiv-Komprimierung und Dekomprimierung, Archive
an entfernten Standorten und Spezialfunktionen, die es erm�glichen, 'tar'
f�r inkrementelle und vollst�ndige Backups einzusetzen. Wenn Sie vorhaben,
Remote-Backups mit tar zu erstellen, dann ben�tigen Sie dazu das rmt-Paket.

%description -l fr
GNU tar sauvegarde plusieurs fichiers sur une seule archive sur bande ou sur
disque et peut restaurer les fichiers individuellement � partir de
l'archive. Il comprend une gestion multi-volumes, la possibilit� d'archiver
des fichiers �parpill�s, la compression/d�compression automatique de
l'archive, les archives distantes et des caract�ristiques sp�ciales
permettant � tar d'�tre utilis� pour des sauvegardes incr�mentales et
compl�tes. Si vous souhaitez faire des sauvegardes distantes avec tar, vous
devrez installer aussi le paquetage � rmt �.

%description -l pl
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
#%patch2 -p0
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p1

install %{SOURCE1} po
%build
chmod -R a+rwX .
gettextize --copy --force
aclocal
automake
autoconf
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
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/tar.info*,%{_mandir}/man1/*} \
	$RPM_BUILD_ROOT%{_mandir}/*/man1/* \
	README NEWS

%find_lang %{name}

%post
/sbin/install-info %{_infodir}/tar.info.gz /etc/info-dir

%preun
if [ $1 = 0 ]; then
	/sbin/install-info --delete %{_infodir}/tar.info.gz /etc/info-dir
fi

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
