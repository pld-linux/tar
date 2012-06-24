Summary:	A GNU file archiving program
Summary(de):	GNU-Magnetband-Archivierprogramm (tar)
Summary(es):	GNU Tape Archiver (tar)
Summary(fr):	Programme d'archivage GNU (tar: GNU Tape Archiver)
Summary(pl):	Program do archiwizacji (GNU)
Summary(pt_BR):	GNU Tape Archiver (tar)
Summary(tr):	Yayg�n kullan�lan yedekleyici
Name:		tar
Version:	1.13.25
Release:	7
Epoch:		1
License:	GPL
Group:		Applications/Archiving
Source0:	ftp://alpha.gnu.org/gnu/tar/%{name}-%{version}.tar.gz
# Source0-md5:	6ef8c906e81eee441f8335652670ac4a
Source1:	%{name}-non-english-man-pages.tar.bz2
# Source1-md5: 	4e4b1655fe42c27a4eb5d7bcd82e74ac
Patch0:		%{name}-man_from_debian_tar_1.13.25-2.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-pipe.patch
Patch3:		%{name}-namecache.patch
Patch4:		%{name}-error.patch
Patch5:		%{name}-sock.patch
Patch6:		%{name}-nolibrt.patch
Patch7:		%{name}-man.patch
Patch8:		%{name}-ac25x.patch
Patch9:		%{name}-dots.patch
Patch10:	%{name}-pl.po-fix.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_bindir		/bin
%define		_libexecdir	/sbin

%description
The GNU tar program saves many files together into one archive and can
restore individual files (or all of the files) from the archive. Tar
can also be used to add supplemental files to an archive and to update
or list files in the archive.

Tar includes multivolume support, automatic archive compression/
decompression, the ability to perform remote archives and the ability
to perform incremental and full backups.

If you want to use Tar for remote backups, you'll also need to install
the rmt package.

%description -l de
Das GNU tar-Programm speichert mehrere Dateien in ein Archiv, und kann
einzelne Dateien daraus wiederherstellen (oder auch alle Dateien). Tar
kann auch benutzt werden, um einem Archiv Dateien hinzuzuf�gen, und um
die Liste der Dateien im Archiv anzuzeigen oder zu ver�ndern.

Tar enth�lt multivolume-Support, automatische
Archivkompression/dekompression, the M�glichkeit, Dateien per Netzwerk
zu archivieren und die M�glichkeit zu inkrementellen backups.

Wenn Sie tar f�r Netzwerkbackups benutzen wollen, brauchen Sie
au�erdem das rmt-Paket.

%description -l es
GNU "tar" guarda varios archivos juntos, en una cinta o archivo de
disco, y puede restaurar archivos individuales de este almacenaje.
Incluye soporte para multivol�menes, habilidad de almacenar archivos
dispersos, compresi�n/descompresi�n autom�tica, almacenajes remotos y
caracter�sticas especiales que permiten "tar" ser usado para backups
incrementales y completos. Si deseas hacer backups remotos con tar, te
har� falta instalar el paquete "rmt".

%description -l fr
Le programme GNU tar permet de regrouper plusieurs fichiers en une
seule archive et d'effectuer diverses op�rations sur cette archive
(extraction d'un fichier particulier, mise � jour, ajout d'un nouveau
fichier, ...).

Tar g�re les archives multi-volumes, la compression et la
d�compression de mani�re transparente ainsi que la possibilit� de
r�aliser des sauvegardes incr�mentales et des sauvegardes compl�tes.

Si vous comptez utiliser Tar pour des sauvegardes distantes, vous
devriez �galement installer le programme rmt.

Tar devrait �tre install� sur tout syst�me car ses capacit� de
(d�)compression sont essentielles pour travailler sur les fichiers.

%description -l pl
Program GNU tar s�u�y do zapisywania wielu plik�w w pojedynczym
archiwum i moze tak�e s�u�y� do odzyskiwania z tak prepaowanych
archiw�w pojedynczych plik�w (lub wszystkich). Za jego pomoc� mo�na
tak�e dodwa� nowe pliki do ju� istiej�cego archiwum.

GNU tar umo�liwia robienie wielocz�ciowych archiw�w (multivolume
archive), automatyczn� kompresj� i dekompresj� samego archiwum a tak�e
ma mo�liwo�� operowania na zdalnych archiiwach co jest przydatne przy
sporz�dzaniu przyrostowych i pe�nych archiw�w zasob�w.

Je�eli zamierzasz u�ywa� rprogramu tar do operowania na zdalnych
archiwach powiniene� doinstalowa� pakiet rmt.

GNU tar s�u�y do zapisywania wielu plik�w na ta�m� lub dysk. Mo�e
odtwarza� pojedy�cze pliki z archiwum. Umo�liwia zapis du�ego archiwum
z podzia�em na wiele no�nik�w. Tar obs�uguje tak�e automatyczn�
kompresj�/dekompresj� i archiwa zdalne. Posiada specjalne opcje do
robienia pe�nych i przyrostowych kopii bezpiecze�stwa. Aby tworzy�
zdalne archiwa tar-a trzeba zainstalowa� pakiet rmt.

%description -l pt_BR
GNU "tar" guarda v�rios arquivos juntos em uma fita ou arquivo de
disco, e pode restaurar arquivos individuais desta armazenagem. Ele
inclui suporte para multi-volumes, habilidade de armazenar arquivos
dispersos, compress�o/descompress�o autom�tica, armazenamentos remotos
e caracter�sticas especiais que permitem "tar" ser usado para backups
incrementais e completos. Se voc� deseja fazer backups remotos com
tar, voc� ir� precisar instalar o pacote "rmt".

%description -l tr
GNU tar, birden �ok dosyay� tek bir manyetik bant ya da disk �zerinde
ar�ivleyebildi�i gibi, bu dosyalar�n ar�ivden tek tek geri
y�klenmesine de izin verir. �ok k�s�ml� ar�ivleri, otomatik ar�iv
s�k��t�rma ve a�may�, uzak ar�ivleri, art�msal yedeklemeyi destekler.

%prep
%setup -q
%patch0 -p2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p0
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
chmod -R a+rwX .
rm -f missing m4/{ccstdc,codeset,gettext,glibc21,iconv,isc-posix,lcmessage,progtest,ulonglong}.m4
%{__autoheader}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure

cd doc
cp -f stamp-vti version.texi
touch *
makeinfo --force tar.texi
cd ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/bin,%{_mandir}/man1}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

ln -sf %{_bindir}/tar $RPM_BUILD_ROOT/usr/bin/gtar
install tar.1 $RPM_BUILD_ROOT%{_mandir}/man1
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /usr/bin/*
%{_infodir}/tar.info*
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(id) %{_mandir}/id/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
