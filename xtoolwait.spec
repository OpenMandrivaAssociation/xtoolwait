Summary:	A utility which aims to decrease X session startup time
Name:		xtoolwait
Version:	1.3
Release:	16
License:	GPL
Group:		System/Configuration/Other
BuildRequires:	imake
BuildRequires:	pkgconfig(x11)
Buildrequires:	pkgconfig(xext)
Url:		http://www.hacom.nl/~richard/software/xtoolwait.html
Source:		ftp://ftp.x.org/contrib/utilities/%{name}-%{version}.tar.bz2
Patch0:		xtoolwait-imake.patch

%description
Xtoolwait is a utility which starts an X client in the background, waits
for a window to be mapped on the root window, and then exits.  Xtoolwait
can improve performance for users who start a bunch of X clients
automatically (for example, xterm, xlock, xconsole, whatever) when the
X session starts.

Install xtoolwait if you'd like to try to speed up the startup time for
X sessions.

%prep
%setup -q
%patch0 -p1

%build
xmkmf
%make CDEBUGFLAGS="%{optflags}" EXTRA_LDOPTIONS="%{ldflags}"

%install
%{makeinstall_std} install.man

%clean

%files
%{_bindir}/xtoolwait
%{_mandir}/man1/xtoolwait.1*


%changelog
* Fri Jan 21 2011 Funda Wang <fwang@mandriva.org> 1.3-13mdv2011.0
+ Revision: 632065
- br xext
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.3-12mdv2010.0
+ Revision: 435318
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.3-11mdv2009.0
+ Revision: 242997
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- fix man pages extension

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jun 18 2007 Adam Williamson <awilliamson@mandriva.org> 1.3-9mdv2008.0
+ Revision: 40748
- new X.org layout; trim buildrequires; rebuild for new era
- Import xtoolwait



* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.3-8mdk
- Rebuild

* Sat Dec 25 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.3-7mdk
- fix buildrequires
- cosmetics

* Mon Jul 21 2003 Aurelien Lemaire <alemaire@mandrakesoft.com> 1.3-6mdk
- Rebuild for the new RPM
- Add Url

* Mon May 06 2002 Aurelien Lemaire <alemaire@mandrakesoft.com> 1.3-5mdk
- Rebuild

* Tue May 01 2001 David BAUDENS <baudens@mandrakesoft.com> 1.3-4mdk
- Use %%_tmppath for BuildRoot

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.3-3mdk
- automatically added BuildRequires

* Tue Mar 28 2000 dam's <damien@mandrakesoft.com> 1.3-2mdk
- Release.

* Fri Nov 5 1999 dam's <damien@mandrakesoft.com>
- Version 1.3

* Thu May 06 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- build new version for 6.0

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- new version

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
