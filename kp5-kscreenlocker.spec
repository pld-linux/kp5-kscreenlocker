#
# Conditional build:
%bcond_with	tests		# test suite
%bcond_with	consolekit	# ConsoleKit instead of loginctl for emergency session unlocking

%define		qt_ver		5.15.2
%define		kf_ver		5.102.0
%define		kp_ver		%{version}
%define		kpname		kscreenlocker
Summary:	KDE screen locker
Summary(pl.UTF-8):	Blokowanie ekranu dla KDE
Name:		kp5-%{kpname}
Version:	5.27.12
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kp_ver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	a7d72e4e130081000b889b73c3e46303
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5Qml-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5Test-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5X11Extras-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-tools
BuildRequires:	kf5-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf5-kcmutils-devel >= %{kf_ver}
BuildRequires:	kf5-kconfig-devel >= %{kf_ver}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kf_ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kcrash-devel >= %{kf_ver}
BuildRequires:	kf5-kdeclarative-devel >= %{kf_ver}
BuildRequires:	kf5-kglobalaccel-devel >= %{kf_ver}
BuildRequires:	kf5-ki18n-devel >= %{kf_ver}
BuildRequires:	kf5-kidletime-devel >= %{kf_ver}
BuildRequires:	kf5-kio-devel >= %{kf_ver}
BuildRequires:	kf5-knotifications-devel >= %{kf_ver}
BuildRequires:	kf5-kpackage-devel >= %{kf_ver}
BuildRequires:	kf5-kwayland-devel >= %{kf_ver}
BuildRequires:	kf5-kwindowsystem-devel >= %{kf_ver}
BuildRequires:	kf5-kxmlgui-devel >= %{kf_ver}
BuildRequires:	kf5-solid-devel >= %{kf_ver}
BuildRequires:	kp5-layer-shell-qt-devel >= %{kp_ver}
BuildRequires:	kp5-libkscreen-devel >= %{kp_ver}
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel >= 1.3
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xz
Requires:	kf5-kcmutils >= %{kf_ver}
Requires:	kf5-kconfig >= %{kf_ver}
Requires:	kf5-kcoreaddons >= %{kf_ver}
Requires:	kf5-kcrash >= %{kf_ver}
Requires:	kf5-kdeclarative >= %{kf_ver}
Requires:	kf5-kglobalaccel >= %{kf_ver}
Requires:	kf5-ki18n >= %{kf_ver}
Requires:	kf5-kidletime >= %{kf_ver}
Requires:	kf5-kio >= %{kf_ver}
Requires:	kf5-knotifications >= %{kf_ver}
Requires:	kf5-kpackage >= %{kf_ver}
Requires:	kf5-kwayland >= %{kf_ver}
Requires:	kf5-kwindowsystem >= %{kf_ver}
Requires:	kf5-kxmlgui >= %{kf_ver}
Requires:	kf5-solid >= %{kf_ver}
Requires:	kp5-layer-shell-qt-devel >= %{kp_ver}
Requires:	kp5-libkscreen-devel >= %{kp_ver}
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5DBus >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Network >= %{qt_ver}
Requires:	Qt5Qml >= %{qt_ver}
Requires:	Qt5Quick >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	Qt5X11Extras >= %{qt_ver}
Requires:	wayland >= 1.3
%{?with_consolekit:Suggests:	ConsoleKit}
%{?with_consolekit:Suggests:	qt5-dbus}
# systemd or elogind
%{!?with_consolekit:Suggests:	/bin/loginctl}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE screen locker.

%description -l pl.UTF-8
Blokowanie ekranu dla KDE.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qt_ver}
Requires:	Qt5X11Extras-devel >= %{qt_ver}
Requires:	libstdc++-devel >= 6:7

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	%{?with_consolekit:-Dcklistsessions_EXECUTABLE:PATH=/usr/bin/ck-list-sessions} \
	%{?with_consolekit:-Dqdbus_EXECUTABLE:PATH=/usr/bin/qdbus-qt5} \
	%{!?with_consolekit:-Dloginctl_EXECUTABLE:PATH=/bin/loginctl}

%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kpname}5 --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kpname}5.lang
%defattr(644,root,root,755)
%doc DESIGN README.pam
%if %{with consolekit}
%attr(755,root,root) %{_bindir}/ck-unlock-session
%endif
%attr(755,root,root) %{_libexecdir}/kscreenlocker_greet
%attr(755,root,root) %{_libdir}/libKScreenLocker.so.*.*
%ghost %{_libdir}/libKScreenLocker.so.5
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_screenlocker.so
%{_datadir}/dbus-1/interfaces/kf5_org.freedesktop.ScreenSaver.xml
%{_datadir}/dbus-1/interfaces/org.kde.screensaver.xml
%{_datadir}/kconf_update/kscreenlocker.upd
%attr(755,root,root) %{_datadir}/kconf_update/ksreenlocker_5_3_separate_autologin.pl
%{_datadir}/knotifications5/ksmserver.notifyrc
%dir %{_datadir}/ksmserver
%{_datadir}/ksmserver/screenlocker
%{_datadir}/kpackage/kcms/kcm_screenlocker
%{_datadir}/qlogging-categories5/kscreenlocker.categories
%{_desktopdir}/kcm_screenlocker.desktop

%files devel
%defattr(644,root,root,755)
%{_libdir}/libKScreenLocker.so
%{_includedir}/KScreenLocker
%{_libdir}/cmake/KScreenLocker
%dir %{_libdir}/cmake/ScreenSaverDBusInterface
%{_libdir}/cmake/ScreenSaverDBusInterface/ScreenSaverDBusInterfaceConfig.cmake
