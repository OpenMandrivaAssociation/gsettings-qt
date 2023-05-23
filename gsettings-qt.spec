%define debug_package %nil
%define snap	20150325

%define major	1
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}


Summary:	Qml bindings for GSettings
Name:		gsettings-qt
Version:	0.2
Release:	1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/papyros/gsettings-qt
Source0:  https://gitlab.com/ubports/development/core/gsettings-qt/-/archive/v%{version}/gsettings-qt-v%{version}.tar.bz2
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5QuickTest)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)  

%description
Qml bindings for GSettings.

%package -n	%{libname}
Summary:	Qml bindings for GSettings
Group:		System/Libraries

%description -n	%{libname}
Qml bindings for GSettings

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package includes the development files for %{name}.

%prep
%setup -qn %{name}-%{version}
%autopatch -p1

%build
%qmake_qt5
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%{_qt5_libdir}/qt5/qml/
%{_qt5_libdir}/qt5/tests

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%{_qt5_includedir}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
