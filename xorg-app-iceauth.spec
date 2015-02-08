Summary:	iceauth application
Name:		xorg-app-iceauth
Version:	1.0.7
Release:	1
License:	MIT
Group:		X11/Application
Source0:	http://xorg.freedesktop.org/releases/individual/app/iceauth-%{version}.tar.bz2
# Source0-md5:	25dab02f8e40d5b71ce29a07dc901b8c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-libICE-devel
BuildRequires:	xorg-proto
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iceauth application.

%prep
%setup -qn iceauth-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/iceauth
%{_mandir}/man1/iceauth.1x*

