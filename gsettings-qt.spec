%define debug_package %nil
%define snap	20150325

%define major	1
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}


Summary:	Qml bindings for GSettings
Name:		gsettings-qt
Version:	0.0.0
Release:	0.%{snap}.1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/papyros/gsettings-qt
# bzr branch lp:gsettings-q
# bzr export --root=gsettings-qt-0.0.0-$(date +%Y%m%d) ../gsettings-qt-0.0.0-$(date +%Y%m%d).tar.gz
Source0:	%{name}-%{version}-%{snap}.tar.gz
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5QuickTest)
BuildRequires:	pkgconfig(Qt5Qml)

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
%setup -qn %{name}-%{version}-%{snap}
%apply_patches

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
