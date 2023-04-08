#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.12.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		ktp-text-ui
Summary:	ktp-text-ui
Name:		ka5-%{kaname}
Version:	22.12.3
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	5ce10939ac5630c31415ac5672419b0f
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Positioning-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5WebChannel-devel >= 5.11.1
BuildRequires:	Qt5WebEngine-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-ktp-common-internals-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kemoticons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kitemviews-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf5-kservice-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-sonnet-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-qt5-devel >= 0.9.8
BuildRequires:	xz
ExcludeArch:	x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telepathy handler for Text Chats.

%description -l pl.UTF-8
Program obsługi Telepathy do tekstowych czatów.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktp-log-viewer
%attr(755,root,root) %{_libdir}/libktpchat.so
%attr(755,root,root) %{_libdir}/libktpimagesharer.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_ktp_chat_appearance.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_ktp_chat_behavior.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_ktp_chat_messages.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_ktp_chat_otr.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_ktp_logviewer_behavior.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_ktptextui_message_filter_emoticons.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_ktptextui_message_filter_latex.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktptextui_message_filter_bugzilla.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktptextui_message_filter_emoticons.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktptextui_message_filter_formatting.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktptextui_message_filter_geopoint.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktptextui_message_filter_highlight.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktptextui_message_filter_images.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktptextui_message_filter_latex.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktptextui_message_filter_otr.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktptextui_message_filter_searchexpansion.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktptextui_message_filter_tts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktptextui_message_filter_urlexpansion.so
%attr(755,root,root) %{_libdir}/qt5/plugins/ktptextui_message_filter_youtube.so
%attr(755,root,root) %{_libexecdir}/ktp-adiumxtra-protocol-handler
%attr(755,root,root) %{_libexecdir}/ktp-text-ui
%{_desktopdir}/org.kde.ktplogviewer.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.TextUi.service
%{_datadir}/kservices5/adiumxtra.protocol
%{_datadir}/kservices5/kcm_ktp_chat_appearance.desktop
%{_datadir}/kservices5/kcm_ktp_chat_behavior.desktop
%{_datadir}/kservices5/kcm_ktp_chat_messages.desktop
%{_datadir}/kservices5/kcm_ktp_chat_otr.desktop
%{_datadir}/kservices5/kcm_ktp_logviewer_behavior.desktop
%{_datadir}/kservices5/kcm_ktptextui_message_filter_emoticons.desktop
%{_datadir}/kservices5/kcm_ktptextui_message_filter_latex.desktop
%{_datadir}/kservices5/ktptextui_message_filter_bugzilla.desktop
%{_datadir}/kservices5/ktptextui_message_filter_emoticons.desktop
%{_datadir}/kservices5/ktptextui_message_filter_formatting.desktop
%{_datadir}/kservices5/ktptextui_message_filter_geopoint.desktop
%{_datadir}/kservices5/ktptextui_message_filter_highlight.desktop
%{_datadir}/kservices5/ktptextui_message_filter_images.desktop
%{_datadir}/kservices5/ktptextui_message_filter_latex.desktop
%{_datadir}/kservices5/ktptextui_message_filter_otr.desktop
%{_datadir}/kservices5/ktptextui_message_filter_searchexpansion.desktop
%{_datadir}/kservices5/ktptextui_message_filter_tts.desktop
%{_datadir}/kservices5/ktptextui_message_filter_urlexpansion.desktop
%{_datadir}/kservices5/ktptextui_message_filter_youtube.desktop
%{_datadir}/kservicetypes5/ktptxtui_message_filter.desktop
%{_datadir}/ktelepathy
%{_datadir}/ktp-log-viewer
%{_datadir}/kxmlgui5/ktp-text-ui
%{_datadir}/telepathy/clients/KTp.TextUi.client
