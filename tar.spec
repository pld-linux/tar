Summary:	GNU Tape Archiver (tar)
Summary(de):	GNU-Magnetband-Archivierprogramm (tar)
Summary(fr):	Programme d'archivage GNU (tar : GNU Tape Archiver).
Summary(pl):	Program do archiwizacji (GNU)
Summary(tr):	Yaygýn kullanýlan yedekleyici
Name:		tar
Version:	1.12
Release:	10
Copyright:	GPL
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
Source0:	ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Source1:	tar-pl.po.patch
Patch0:		tar-manpage.patch
Patch1:		tar-bzip2.patch
Patch2:		tar-cached_uid.patch
Patch3:		tar-bzip2-locale.patch
Patch4:		tar-info.patch
Patch5:		tar-pipe.patch
Patch6:		tar-namecache.patch
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

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
beinhaltet Multivolume-Support, die Fähigkeit, seltene Dateien zu
archivieren, automatische Archiv-Komprimierung und Dekomprimierung, Archive
an entfernten Standorten und Spezialfunktionen, die es ermöglichen, 'tar'
für inkrementelle und vollständige Backups einzusetzen. Wenn Sie vorhaben,
Remote-Backups mit tar zu erstellen, dann benötigen Sie dazu das rmt-Paket.

%description -l fr
GNU tar sauvegarde plusieurs fichiers sur une seule archive sur bande ou sur
disque et peut restaurer les fichiers individuellement à partir de
l'archive. Il comprend une gestion multi-volumes, la possibilité d'archiver
des fichiers éparpillés, la compression/décompression automatique de
l'archive, les archives distantes et des caractéristiques spéciales
permettant à tar d'être utilisé pour des sauvegardes incrémentales et
complètes. Si vous souhaitez faire des sauvegardes distantes avec tar, vous
devrez installer aussi le paquetage « rmt ».

%description -l pl
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
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p1

install %{SOURCE1} po
%build
LIBS="-lbsd" CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr \
	--bindir=/bin \
	--libexecdir=/sbin

(cd doc; cp stamp-vti version.texi; touch *; makeinfo --force tar.texi)
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}

make prefix=$RPM_BUILD_ROOT/usr bindir=$RPM_BUILD_ROOT/bin libexecdir=$RPM_BUILD_ROOT/sbin install

ln -s ../../bin/tar $RPM_BUILD_ROOT%{_bindir}/gtar
install tar.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf $RPM_BUILD_ROOT/usr/{info/tar.info*,man/man1/*}
gzip -9nf README NEWS

%post
/sbin/install-info %{_infodir}/tar.info.gz /etc/info-dir

%preun
if [ $1 = 0 ]; then
	/sbin/install-info --delete %{_infodir}/tar.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644, root, root, 0755)
%doc NEWS.gz README.gz
%attr(755, root, root) /bin/*
%attr(755, root, root) %{_bindir}/*
%{_infodir}/tar.info*
%{_mandir}/man1/*

%lang(de) %{_datadir}/locale/de/LC_MESSAGES/tar.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/tar.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/tar.mo
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/tar.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/tar.mo
%lang(no) %{_datadir}/locale/no/LC_MESSAGES/tar.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/tar.mo
%lang(pt) %{_datadir}/locale/pt/LC_MESSAGES/tar.mo
%lang(sl) %{_datadir}/locale/sl/LC_MESSAGES/tar.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/tar.mo

%changelog
* Thu Feb 10 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [1.12-8]
- added Group(pl)
- added gzipping documentation
- cosmetic changes

* Mon Dec 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.12-7]
- standarized {un}registering info pages (added tar-info.patch),
- added gzipping man pages.

* Sat Nov 21 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.12-6]
- added {un}registering info page in %post %preun with --entry.

* Mon Sep 21 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.12-5]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- changed passing $RPM_OPT_FLAGS, LIBS and LDFLAGS (now as a configure
  enviroment variable).

* Wed Sep  2 1998 Konrad Stêpieñ <konrad@interdata.com.pl>
  [1.12-5]
- added %%{PACKAGE_VERSION} macros to Buildroot and Source,
- patched to better performaance which unknown uid/gid,
- Source adres changed to regular URL,
- updated pl locales to 1.12,
- added bzip2 support, update man page and pl locales,
- translation for pl,
- changed mkdir to install -d,
- added %doc.

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- add %{_bindir}/gtar symlink (change #421)

* Tue Jul 14 1998 Jeff Johnson <jbj@redhat.com>
- Fiddle bindir/libexecdir to get RH install correct.
- Don't include /sbin/rmt -- use the rmt from dump.
- Turn on nls.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 16 1997 Donnie Barnes <djb@redhat.com>
- updated from 1.11.8 to 1.12
- various spec file cleanups
- /sbin/install-info support

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu May 29 1997 Michael Fulbright <msf@redhat.com>
- Fixed to include rmt
