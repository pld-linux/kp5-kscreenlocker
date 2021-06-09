%define		kdeplasmaver	5.22.0
%define		qtver		5.9.0
%define		kf5ver		5.19.0
%define		kpname		kscreenlocker
Summary:	kscreenlocker
Name:		kp5-%{kpname}
Version:	5.22.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	cfbdaaa3ed30fe1ebbfe62181b52a8c2
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
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
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
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
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

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
%{_datadir}/kservices5/screenlocker.desktop
%attr(755,root,root) %{_prefix}/libexec/kcheckpass
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
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_screenlocker.so
%dir %{_datadir}/kpackage/kcms/kcm_screenlocker
%dir %{_datadir}/kpackage/kcms/kcm_screenlocker/contents
%dir %{_datadir}/kpackage/kcms/kcm_screenlocker/contents/ui
%{_datadir}/kpackage/kcms/kcm_screenlocker/contents/ui/Appearance.qml
%{_datadir}/kpackage/kcms/kcm_screenlocker/contents/ui/LnfConfig.qml
%{_datadir}/kpackage/kcms/kcm_screenlocker/contents/ui/WallpaperConfig.qml
%{_datadir}/kpackage/kcms/kcm_screenlocker/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_screenlocker/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_screenlocker/metadata.json

%files devel
%defattr(644,root,root,755)
%{_includedir}/KScreenLocker
%{_libdir}/cmake/KScreenLocker
%dir %{_libdir}/cmake/ScreenSaverDBusInterface
%{_libdir}/cmake/ScreenSaverDBusInterface/ScreenSaverDBusInterfaceConfig.cmake
%{_libdir}/libKScreenLocker.so
