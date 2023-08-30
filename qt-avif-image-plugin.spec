Summary:	Qt plugin for handling AVIF images
Name:		qt-avif-image-plugin
License:	GPLv3
Version:	0.5.4
Release:	1
Source0:	https://github.com/novomesk/qt-avif-image-plugin/archive/v%{version}/%{name}-%{version}.tar.gz

# Fix build with newly released libavif 1.0.0
Patch0:		https://github.com/novomesk/qt-avif-image-plugin/commit/bd2c8a47fd04ad38f0b00c7c8648cd723006fd81.patch

BuildRequires:	cmake ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	pkgconfig(libavif)
BuildRequires:	qt5-macros
BuildRequires:	qmake5
Supplements:	%mklibname qt5gui 5

%description
Qt plugin for handling AVIF images

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

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_libdir}/qt5/plugins/imageformats/libqavif5.so
