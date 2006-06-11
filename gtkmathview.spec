Summary:	A GTK+ viewer to view MathML documents
Summary(pl):	Przegl±darka dokumentów MathML dla GTK+
Name:		gtkmathview
Version:	0.7.6
Release:	2
License:	GPL v2+
Group:		X11/Applications/Graphics
#Source0Download: http://helm.cs.unibo.it/mml-widget/
Source0:	http://www.cs.unibo.it/helm/mml-widget/sources/%{name}-%{version}.tar.gz
# Source0-md5:	4bb348c98367228f0de0a2216a13d48f
Patch0:		%{name}-no_static_viewer.patch
URL:		http://helm.cs.unibo.it/mml-widget/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.9.2
BuildRequires:	gdome2-cpp_smart-devel >= 0.1.8
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxslt-progs >= 1.1.17
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	t1lib-devel >= 1.2
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkMathView is a GTK+ Widget for rendering MathML documents.

%description -l pl
GtkMathView jest przegl±dark± MathML dla GTK+.

%package libs
Summary:	A GTK+ Widget for rendering MathML documents
Summary(pl):	Biblioteki GTK+ Widget do renderowania dokumentów MathML
Group:		Development/Libraries
Requires:	gdome2-cpp_smart >= 0.1.8
Requires:	gtk+2 >= 1:2.2.0

%description libs
GTK+ Widgets for rendering MathML documents.

%description libs -l pl
Biblioteki GTK+ Widget do renderowania dokumentów MathML.

%package devel
Summary:	A GTK+ Widget for rendering MathML documents - header files
Summary(pl):	Biblioteki GTK+ Widget do renderowania dokumentów MathML - pliki nag³ówkowe
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gdome2-cpp_smart-devel >= 0.1.8
Requires:	gtk+2-devel >= 2:2.9.2
Requires:	libxml2-devel >= 1:2.6.26

%description devel
Header files for GTK+ Widgets for rendering MathML documents.

%description devel -l pl
Pliki nag³ówkowe dla GTK+ Widget do renderowania dokumentów MathML.

%package static
Summary:	A GTK+ Widget for rendering MathML documents - static library
Summary(pl):	Biblioteki GTK+ Widget do renderowania dokumentów MathML - wersja statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version libraries for GTK+ for rendering MathML documents.

%description static -l pl
Wersja statyczna bibliotek dla GTK+ do renderowania dokumentów MathML.

%prep
%setup -q
%patch0 -p1

echo 'm4_pattern_allow(AM_BINRELOC)' > acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-libxml2 \
	--enable-stats \
	--with-t1lib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CONTRIBUTORS ChangeLog HISTORY LICENSE NEWS README TODO
%attr(755,root,root) %{_bindir}/mathmlviewer
%attr(755,root,root) %{_bindir}/mathmlsvg
%{_mandir}/man1/math*.1*
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_sysconfdir}/gtkmathview
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtkmathview/gtkmathview.conf.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
