%define major		1
%define libname		%mklibname xxf86vm %{major}
%define develname	%mklibname xxf86vm -d

Name:		libxxf86vm
Summary:	XFree86 Video Mode Extension Library
Version:	1.1.2
Release:	1
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86vm-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 7.5
BuildRequires: x11-util-macros >= 1.0.1

%description
XFree86 Video Mode Extension Library

%package -n %{libname}
Summary: Shared libraries for %{name}
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
XFree86 Video Mode Extension Library

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0
Conflicts: x11-proto-devel < 7.5
Obsoletes: %{_lib}xxf86vm1-devel
Obsoletes: %{_lib}xxf86vm-static-devel

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXxf86vm-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXxf86vm.so.%{major}*

%files -n %{develname}
%{_libdir}/libXxf86vm.so
%{_libdir}/pkgconfig/xxf86vm.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/XF86VidMode*.*
%{_mandir}/man3/XF86VM.*

