#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.10
%define		qtver		5.15.2
%define		kf5ver		5.19.0
%define		kpname		kscreenlocker
Summary:	kscreenlocker
Name:		kp5-%{kpname}
Version:	5.27.10
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	c44cfe3ba7fb03fc30b2ae305f16ed79
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	kf5-kcmutils-devel >= %{kf5ver}
BuildRequires:	kf5-kcrash-devel >= %{kf5ver}
BuildRequires:	kf5-kdeclarative-devel >= %{kf5ver}
BuildRequires:	kf5-kdelibs4support-devel >= %{kf5ver}
BuildRequires:	kf5-kglobalaccel-devel >= %{kf5ver}
BuildRequires:	kf5-kidletime-devel >= %{kf5ver}
BuildRequires:	kf5-kwayland-devel
BuildRequires:	kf5-plasma-framework-devel >= %{kf5ver}
BuildRequires:	kp5-layer-shell-qt-devel >= %{kdeplasmaver}
BuildRequires:	kp5-libkscreen-devel >= %{kdeplasmaver}
BuildRequires:	ninja
BuildRequires:	pam-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
kscreenlocker

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

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
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}5.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/libexec/kscreenlocker_greet
%ghost %{_libdir}/libKScreenLocker.so.5
%attr(755,root,root) %{_libdir}/libKScreenLocker.so.*.*
%{_datadir}/dbus-1/interfaces/kf5_org.freedesktop.ScreenSaver.xml
%{_datadir}/dbus-1/interfaces/org.kde.screensaver.xml
%{_datadir}/kconf_update/kscreenlocker.upd
%attr(755,root,root) %{_datadir}/kconf_update/ksreenlocker_5_3_separate_autologin.pl
%{_datadir}/knotifications5/ksmserver.notifyrc
%dir %{_datadir}/ksmserver
%dir %{_datadir}/ksmserver/screenlocker
%dir %{_datadir}/ksmserver/screenlocker/org.kde.passworddialog
%{_datadir}/ksmserver/screenlocker/org.kde.passworddialog/metadata.desktop
%dir %{_datadir}/kpackage/kcms/kcm_screenlocker
%dir %{_datadir}/kpackage/kcms/kcm_screenlocker/contents
%dir %{_datadir}/kpackage/kcms/kcm_screenlocker/contents/ui
%{_datadir}/kpackage/kcms/kcm_screenlocker/contents/ui/Appearance.qml
%{_datadir}/kpackage/kcms/kcm_screenlocker/contents/ui/LnfConfig.qml
%{_datadir}/kpackage/kcms/kcm_screenlocker/contents/ui/WallpaperConfig.qml
%{_datadir}/kpackage/kcms/kcm_screenlocker/contents/ui/main.qml
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_screenlocker.so
%{_desktopdir}/kcm_screenlocker.desktop
%{_datadir}/qlogging-categories5/kscreenlocker.categories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KScreenLocker
%{_libdir}/cmake/KScreenLocker
%dir %{_libdir}/cmake/ScreenSaverDBusInterface
%{_libdir}/cmake/ScreenSaverDBusInterface/ScreenSaverDBusInterfaceConfig.cmake
%{_libdir}/libKScreenLocker.so
