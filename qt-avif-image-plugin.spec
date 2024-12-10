Summary:	Qt plugin for handling AVIF images
Name:		qt-avif-image-plugin
License:	GPLv3
Version:	0.8.7
Release:	1
Source0:	https://github.com/novomesk/qt-avif-image-plugin/archive/v%{version}/%{name}-%{version}.tar.gz


BuildRequires:	cmake ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	pkgconfig(libavif)
BuildRequires:	qt5-macros
BuildRequires:	qmake5
Supplements:	%mklibname qt5gui 5

BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6DBusTools)
BuildRequires:	cmake(Qt6Gui)

%description
Qt plugin for handling AVIF images

%package qt6
Summary:	Qt 6 plugin for handling AVIF images
Group:		System/Libraries
Supplements:	%mklibname Qt6Gui

%description qt6
Qt 6 plugin for handling AVIF images

%prep
%autosetup -p1 -n %{name}-%{version}

# ECM seems to require a metainfo file these days
cat >metainfo.yaml <<EOF
description: %{summary}
platforms:
    - name: Linux
portingAid: false
deprecated: false
release: true
public_lib: true
EOF

%cmake_qt5 \
	-DKDE_INSTALL_QTPLUGINDIR:PATH=%{_libdir}/qt5/plugins \
	-G Ninja

cd ..
export CMAKE_BUILD_DIR=build-qt6
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%ninja_build -C build-qt6

%install
%ninja_install -C build

%ninja_install -C build-qt6

%files
%{_libdir}/qt5/plugins/imageformats/libqavif5.so

%files qt6
%{_libdir}/qt6/plugins/imageformats/libqavif6.so
