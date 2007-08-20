%define name	xtoolwait
%define version	1.3
%define release	%mkrel 9

Summary:	A utility which aims to decrease X session startup time
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Configuration/Other
BuildRequires:	XFree86-devel imake libx11-devel libxext-devel
Url:		http://www.hacom.nl/~richard/software/xtoolwait.html
Source:		ftp://ftp.x.org/contrib/utilities/%{name}-%{version}.tar.bz2
Patch0:		xtoolwait-imake.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std} install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/xtoolwait
%{_mandir}/man1/xtoolwait.1*
