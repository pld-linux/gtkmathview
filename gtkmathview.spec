Summary:	A GTK viewer to view MathML documents
Summary(pl):	Przegl±darka dokumentów MathML dla GTK
Name:		gtkmathview
Version:	0.6.3
Release:	0.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.cs.unibo.it/helm/mml-widget/sources/%{name}-%{version}.tar.gz
BuildRequires:	atk-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gdome2-cpp_smart-devel
BuildRequires:	libxml2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	t1lib-devel >= 1.2
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkMathView is a GTK Widget for rendering MathML documents.

%description -l pl
GtkMathView jest przegl±dark± MathML dla GTK.

%package libs
Summary:	A GTK Widget for rendering MathML documents
Summary(pl):	Biblioteki GTK Widget do renderowania dokumentów MathML
Group:		Development/Libraries

%description libs
GTK Widgets for rendering MathML documents.

%description libs -l pl
Biblioteki GTK Widget do renderowania dokumentów MathML.

%package devel
Summary:	A GTK Widget for rendering MathML documents - header files.
Summary(pl):	Biblioteki GTK Widget do renderowania dokumentów MathML - pliki nag³ówkowe.
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for GTK Widgets for rendering MathML documents.

%description devel -l pl
Pliki nag³ówkowe dla GTK Widget do renderowania dokumentów MathML.

%package static
Summary:	A GTK Widget for rendering MathML documents - static library
Summary(pl):	Biblioteki GTK Widget do renderowania dokumentów MathML - wersja statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version libraries for GTK for rendering MathML documents.

%description static -l pl
Wersja statyczna bibliotek dla GTK do renderowania dokumentów MathML.

%prep
%setup -q

%build
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

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog HISTORY INSTALL LICENSE NEWS README TODO
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
