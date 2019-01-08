%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		ktp-text-ui
Summary:	ktp-text-ui
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	900b5898acd77d10d9d35c2e9d208f0b
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
BuildRequires:	ka5-ktp-common-internals-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.7.0
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kemoticons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-sonnet-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-qt5-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telepathy handler for Text Chats.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

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
