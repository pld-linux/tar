#
# Conditional build:
%bcond_with	tests	# perform make check

Summary:	A GNU file archiving program
Summary(de.UTF-8):	GNU-Magnetband-Archivierprogramm (tar)
Summary(es.UTF-8):	GNU Tape Archiver (tar)
Summary(fr.UTF-8):	Programme d'archivage GNU (tar: GNU Tape Archiver)
Summary(pl.UTF-8):	Program do archiwizacji (GNU)
Summary(pt_BR.UTF-8):	GNU Tape Archiver (tar)
Summary(tr.UTF-8):	Yaygın kullanılan yedekleyici
Name:		tar
Version:	1.25
Release:	1.1
Epoch:		1
License:	GPL v3+
Group:		Applications/Archiving
Source0:	http://ftp.gnu.org/gnu/tar/%{name}-%{version}.tar.bz2
# Source0-md5:	6e497f861c77bbba2f7da4e10270995b
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	4e4b1655fe42c27a4eb5d7bcd82e74ac
Patch0:		%{name}-info.patch
Patch1:		%{name}-pl.po-update.patch
Patch2:		%{name}-zero-block.patch
Patch3:		%{name}-listed-incremental.patch
URL:		http://www.gnu.org/software/tar/tar.html
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	bison
BuildRequires:	gettext-devel >= 0.16
BuildRequires:	help2man
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo
Conflicts:	amanda-client < 2.5.2
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

%description -l de.UTF-8
Das GNU tar-Programm speichert mehrere Dateien in ein Archiv, und kann
einzelne Dateien daraus wiederherstellen (oder auch alle Dateien). Tar
kann auch benutzt werden, um einem Archiv Dateien hinzuzufügen, und um
die Liste der Dateien im Archiv anzuzeigen oder zu verändern.

Tar enthält multivolume-Support, automatische
Archivkompression/dekompression, the Möglichkeit, Dateien per Netzwerk
zu archivieren und die Möglichkeit zu inkrementellen backups.

Wenn Sie tar für Netzwerkbackups benutzen wollen, brauchen Sie
außerdem das rmt-Paket.

%description -l es.UTF-8
GNU "tar" guarda varios archivos juntos, en una cinta o archivo de
disco, y puede restaurar archivos individuales de este almacenaje.
Incluye soporte para multivolúmenes, habilidad de almacenar archivos
dispersos, compresión/descompresión automática, almacenajes remotos y
características especiales que permiten "tar" ser usado para backups
incrementales y completos. Si deseas hacer backups remotos con tar, te
hará falta instalar el paquete "rmt".

%description -l fr.UTF-8
Le programme GNU tar permet de regrouper plusieurs fichiers en une
seule archive et d'effectuer diverses opérations sur cette archive
(extraction d'un fichier particulier, mise à jour, ajout d'un nouveau
fichier, ...).

Tar gère les archives multi-volumes, la compression et la
décompression de manière transparente ainsi que la possibilité de
réaliser des sauvegardes incrémentales et des sauvegardes complètes.

Si vous comptez utiliser Tar pour des sauvegardes distantes, vous
devriez également installer le programme rmt.

Tar devrait être installé sur tout système car ses capacité de
(dé)compression sont essentielles pour travailler sur les fichiers.

%description -l pl.UTF-8
Program GNU tar służy do zapisywania wielu plików w pojedynczym
archiwum i może także służyć do odzyskiwania z tak preparowanych
archiwów pojedynczych plików (lub wszystkich). Za jego pomocą można
także dodawać nowe pliki do już istniejącego archiwum.

GNU tar umożliwia robienie wieloczęściowych archiwów (multivolume
archive), automatyczną kompresję i dekompresję samego archiwum a także
ma możliwość operowania na zdalnych archiwach co jest przydatne przy
sporządzaniu przyrostowych i pełnych archiwów zasobów.

Jeżeli zamierzasz używać programu tar do operowania na zdalnych
archiwach powinieneś doinstalować pakiet rmt.

GNU tar służy do zapisywania wielu plików na taśmę lub dysk. Może
odtwarzać pojedyncze pliki z archiwum. Umożliwia zapis dużego archiwum
z podziałem na wiele nośników. Tar obsługuje także automatyczną
kompresję/dekompresję i archiwa zdalne. Posiada specjalne opcje do
robienia pełnych i przyrostowych kopii bezpieczeństwa. Aby tworzyć
zdalne archiwa tar-a trzeba zainstalować pakiet rmt.

%description -l pt_BR.UTF-8
GNU "tar" guarda vários arquivos juntos em uma fita ou arquivo de
disco, e pode restaurar arquivos individuais desta armazenagem. Ele
inclui suporte para multi-volumes, habilidade de armazenar arquivos
dispersos, compressão/descompressão automática, armazenamentos remotos
e características especiais que permitem "tar" ser usado para backups
incrementais e completos. Se você deseja fazer backups remotos com
tar, você irá precisar instalar o pacote "rmt".

%description -l tr.UTF-8
GNU tar, birden çok dosyayı tek bir manyetik bant ya da disk üzerinde
arşivleyebildiği gibi, bu dosyaların arşivden tek tek geri
yüklenmesine de izin verir. Çok kısımlı arşivleri, otomatik arşiv
sıkıştırma ve açmayı, uzak arşivleri, artımsal yedeklemeyi destekler.

%package rmt
Summary:	tar's version of rmt utility
Summary(pl.UTF-8):	Narzędzie rmt z pakietu tar
Group:		Applications/Archiving

%description rmt
This package provdes rmt utility which can be used instead of the one
coming from dump project.

%description rmt -l pl.UTF-8
Pakiet ten dostarcza narzędzie rmt, które może być użyte zamiast tego
z pakietu dump.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__rm} po/stamp-po

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/bin,%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf %{_bindir}/tar $RPM_BUILD_ROOT/usr/bin/gtar

help2man ./src/tar -o tar.1
install tar.1 $RPM_BUILD_ROOT%{_mandir}/man1
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/tar
%attr(755,root,root) /usr/bin/gtar
%{_infodir}/tar.info*
%{_mandir}/man1/tar.1*
%lang(de) %{_mandir}/de/man1/tar.1*
%lang(es) %{_mandir}/es/man1/tar.1*
%lang(fi) %{_mandir}/fi/man1/tar.1*
%lang(fr) %{_mandir}/fr/man1/tar.1*
%lang(hu) %{_mandir}/hu/man1/tar.1*
%lang(id) %{_mandir}/id/man1/tar.1*
%lang(it) %{_mandir}/it/man1/tar.1*
%lang(ja) %{_mandir}/ja/man1/tar.1*
%lang(nl) %{_mandir}/nl/man1/tar.1*
%lang(pl) %{_mandir}/pl/man1/tar.1*

%files rmt
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/rmt
