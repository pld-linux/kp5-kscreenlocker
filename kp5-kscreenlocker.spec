%define		kdeplasmaver	5.14.4
%define		qtver		5.5.1
%define		kf5ver		5.19.0
%define		kpname		kscreenlocker

Summary:	kscreenlocker
Name:		kp5-%{kpname}
Version:	5.14.4
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	f46412c02e11d53723c89a1f7505a3dd
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
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %ghost %{_libdir}/libKScreenLocker.so.5
%attr(755,root,root) %{_libdir}/libKScreenLocker.so.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/screenlocker_kcm.so
%{_datadir}/dbus-1/interfaces/kf5_org.freedesktop.ScreenSaver.xml
%{_datadir}/dbus-1/interfaces/org.kde.screensaver.xml
%{_datadir}/kconf_update/kscreenlocker.upd
%attr(755,root,root) %{_datadir}/kconf_update/ksreenlocker_5_3_separate_autologin.pl
%{_datadir}/knotifications5/ksmserver.notifyrc
#%%{_datadir}/kservices5/plasma-screenlocker_kcm-screenlocker_kcm.desktop
%dir %{_datadir}/ksmserver/screenlocker
%dir %{_datadir}/ksmserver/screenlocker/org.kde.passworddialog
%{_datadir}/ksmserver/screenlocker/org.kde.passworddialog/metadata.desktop
#%%dir %{_datadir}/plasma/kcms
#%%dir %{_datadir}/plasma/kcms/screenlocker_kcm
#%%dir %{_datadir}/plasma/kcms/screenlocker_kcm/contents
#%%dir %{_datadir}/plasma/kcms/screenlocker_kcm/contents/ui
#%%{_datadir}/plasma/kcms/screenlocker_kcm/contents/ui/main.qml
#%%{_datadir}/plasma/kcms/screenlocker_kcm/metadata.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KScreenLocker
%{_libdir}/cmake/KScreenLocker
%dir %{_libdir}/cmake/ScreenSaverDBusInterface
%{_libdir}/cmake/ScreenSaverDBusInterface/ScreenSaverDBusInterfaceConfig.cmake
%{_libdir}/libKScreenLocker.so
