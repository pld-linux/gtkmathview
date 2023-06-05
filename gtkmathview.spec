Summary:	A GTK+ viewer to view MathML documents
Summary(pl.UTF-8):	Przeglądarka dokumentów MathML dla GTK+
Name:		gtkmathview
Version:	0.8.0
Release:	11
License:	LGPL v3+
Group:		X11/Applications/Graphics
Source0:	http://helm.cs.unibo.it/mml-widget/sources/%{name}-%{version}.tar.gz
# Source0-md5:	b53564e553728d4b69f7d366dfeb5299
Patch0:		%{name}-no_static_viewer.patch
Patch1:		%{name}-gcc.patch
Patch2:		gcc44.patch
Patch3:		gcc47.patch
Patch4:		%{name}-marshalling-functions-git7d938a.patch
Patch5:		%{name}-fix-ComputerModernShaper-git210206.patch
Patch6:		%{name}-lowercasegreek-gitb03152.patch
Patch7:		%{name}-t1lib-private.patch
Patch8:		%{name}-gcc6.patch
Patch9:		%{name}-gcc7.patch
Patch10:	%{name}-fix-cpp-headers.patch
Patch11:	%{name}-link.patch
URL:		http://helm.cs.unibo.it/mml-widget/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gdome2-cpp_smart-devel >= 0.1.8
BuildRequires:	glib2-devel >= 1:2.2.1
BuildRequires:	gtk+2-devel >= 1:2.10.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pangox-compat-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	t1lib-x-devel >= 1.2
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkMathView is a GTK+ Widget for rendering MathML documents.

%description -l pl.UTF-8
GtkMathView jest przeglądarką MathML dla GTK+.

%package libs
Summary:	A GTK+ Widget for rendering MathML documents
Summary(pl.UTF-8):	Biblioteki GTK+ Widget do renderowania dokumentów MathML
Group:		Development/Libraries
Requires:	gdome2-cpp_smart >= 0.1.8
Requires:	glib2 >= 1:2.2.1
Requires:	gtk+2 >= 2:2.10.0
Requires:	libxml2 >= 1:2.6.26

%description libs
GTK+ Widgets for rendering MathML documents.

%description libs -l pl.UTF-8
Biblioteki GTK+ Widget do renderowania dokumentów MathML.

%package devel
Summary:	A GTK+ Widget for rendering MathML documents - header files
Summary(pl.UTF-8):	Biblioteki GTK+ Widget do renderowania dokumentów MathML - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gdome2-cpp_smart-devel >= 0.1.8
Requires:	glib2-devel >= 1:2.2.1
Requires:	gtk+2-devel >= 2:2.10.0
Requires:	libxml2-devel >= 1:2.6.26

%description devel
Header files for GTK+ Widgets for rendering MathML documents.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla GTK+ Widget do renderowania dokumentów MathML.

%package static
Summary:	A GTK+ Widget for rendering MathML documents - static library
Summary(pl.UTF-8):	Biblioteki GTK+ Widget do renderowania dokumentów MathML - wersja statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version libraries for GTK+ for rendering MathML documents.

%description static -l pl.UTF-8
Wersja statyczna bibliotek dla GTK+ do renderowania dokumentów MathML.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

# AM_BINRELOC missing, just ignore
echo 'AC_DEFUN([AM_BINRELOC], [])' > acinclude.m4

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

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCEMENT AUTHORS BUGS CONTRIBUTORS ChangeLog HISTORY LICENSE NEWS README TODO
%attr(755,root,root) %{_bindir}/mathmlps
%attr(755,root,root) %{_bindir}/mathmlsvg
%attr(755,root,root) %{_bindir}/mathmlviewer
%{_mandir}/man1/mathmlviewer.1*
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkmathview_custom_reader.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkmathview_custom_reader.so.0
%attr(755,root,root) %{_libdir}/libgtkmathview_gmetadom.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkmathview_gmetadom.so.0
%attr(755,root,root) %{_libdir}/libgtkmathview_libxml2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkmathview_libxml2.so.0
%attr(755,root,root) %{_libdir}/libgtkmathview_libxml2_reader.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkmathview_libxml2_reader.so.0
%attr(755,root,root) %{_libdir}/libmathview.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmathview.so.0
%attr(755,root,root) %{_libdir}/libmathview_backend_gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmathview_backend_gtk.so.0
%attr(755,root,root) %{_libdir}/libmathview_backend_ps.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmathview_backend_ps.so.0
%attr(755,root,root) %{_libdir}/libmathview_backend_svg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmathview_backend_svg.so.0
%attr(755,root,root) %{_libdir}/libmathview_frontend_custom_reader.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmathview_frontend_custom_reader.so.0
%attr(755,root,root) %{_libdir}/libmathview_frontend_gmetadom.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmathview_frontend_gmetadom.so.0
%attr(755,root,root) %{_libdir}/libmathview_frontend_libxml2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmathview_frontend_libxml2.so.0
%attr(755,root,root) %{_libdir}/libmathview_frontend_libxml2_reader.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmathview_frontend_libxml2_reader.so.0
%dir %{_sysconfdir}/gtkmathview
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtkmathview/gtkmathview.conf.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkmathview_custom_reader.so
%attr(755,root,root) %{_libdir}/libgtkmathview_gmetadom.so
%attr(755,root,root) %{_libdir}/libgtkmathview_libxml2.so
%attr(755,root,root) %{_libdir}/libgtkmathview_libxml2_reader.so
%attr(755,root,root) %{_libdir}/libmathview.so
%attr(755,root,root) %{_libdir}/libmathview_backend_gtk.so
%attr(755,root,root) %{_libdir}/libmathview_backend_ps.so
%attr(755,root,root) %{_libdir}/libmathview_backend_svg.so
%attr(755,root,root) %{_libdir}/libmathview_frontend_custom_reader.so
%attr(755,root,root) %{_libdir}/libmathview_frontend_gmetadom.so
%attr(755,root,root) %{_libdir}/libmathview_frontend_libxml2.so
%attr(755,root,root) %{_libdir}/libmathview_frontend_libxml2_reader.so
%{_pkgconfigdir}/gtkmathview-custom-reader.pc
%{_pkgconfigdir}/gtkmathview-gmetadom.pc
%{_pkgconfigdir}/gtkmathview-libxml2.pc
%{_pkgconfigdir}/gtkmathview-libxml2-reader.pc
%{_pkgconfigdir}/mathview-backend-gtk.pc
%{_pkgconfigdir}/mathview-backend-ps.pc
%{_pkgconfigdir}/mathview-backend-svg.pc
%{_pkgconfigdir}/mathview-core.pc
%{_pkgconfigdir}/mathview-frontend-custom-reader.pc
%{_pkgconfigdir}/mathview-frontend-gmetadom.pc
%{_pkgconfigdir}/mathview-frontend-libxml2.pc
%{_pkgconfigdir}/mathview-frontend-libxml2-reader.pc
%{_includedir}/gtkmathview

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkmathview_custom_reader.a
%{_libdir}/libgtkmathview_gmetadom.a
%{_libdir}/libgtkmathview_libxml2.a
%{_libdir}/libgtkmathview_libxml2_reader.a
%{_libdir}/libmathview.a
%{_libdir}/libmathview_backend_gtk.a
%{_libdir}/libmathview_backend_ps.a
%{_libdir}/libmathview_backend_svg.a
%{_libdir}/libmathview_frontend_custom_reader.a
%{_libdir}/libmathview_frontend_gmetadom.a
%{_libdir}/libmathview_frontend_libxml2.a
%{_libdir}/libmathview_frontend_libxml2_reader.a
