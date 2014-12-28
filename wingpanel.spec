%define		rel		1
%define		subver	alpha2
Summary:	Wing Panel
Name:		wingpanel
Version:	0.1
Release:	0.%{subver}.%{rel}
License:	GPL v3
Group:		X11/Applications
Source0:	https://launchpad.net/wingpanel/0.x/%{version}-%{subver}/+download/%{name}-%{version}-%{subver}.tar.gz
# Source0-md5:	2bbeb2c1b9adb580e246580a493e4a0d
URL:		https://launchpad.net/wingpanel/
BuildRequires:	cmake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
BuildRequires:	granite-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libgee0.6-devel
BuildRequires:	libindicator-gtk3-devel
BuildRequires:	pkgconfig
BuildRequires:	vala >= 0.10.0
BuildRequires:	xorg-lib-libX11-devel
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stylish top panel that holds indicators and spawns an application
launcher.

%prep
%setup -qc

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install -C build \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/sma

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_desktop_database
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/wingpanel
%{_desktopdir}/wingpanel.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.gschema.xml
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/wingpanel.*
