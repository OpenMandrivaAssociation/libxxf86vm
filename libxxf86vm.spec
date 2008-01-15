%define major		1
%define libname		%mklibname xxf86vm %major
%define develname	%mklibname xxf86vm -d
%define staticname	%mklibname xxf86vm -d -s

Name:		libxxf86vm
Summary:	XFree86 Video Mode Extension Library
Version:	1.0.1
Release:	%mkrel 3
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86vm-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: x11-util-macros		>= 1.1.5
BuildRequires: libx11-devel		>= 1.1.3
BuildRequires: libxdmcp-devel		>= 1.0.2
BuildRequires: libxau-devel		>= 1.0.3
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: libxext-devel		>= 1.0.3

%description
XFree86 Video Mode Extension Library

#-----------------------------------------------------------

%package -n %{libname}
Summary: Shared libraries for %{name}
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
XFree86 Video Mode Extension Library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libname} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: %{name}-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %{mklibname xxf86vm 1 -d}

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXxf86vm.so
%{_libdir}/libXxf86vm.la
%{_libdir}/pkgconfig/xxf86vm.pc
%{_mandir}/man3/XF86VidMode*.*
%{_mandir}/man3/XF86VM.*

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: %{name}-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0
Obsoletes: %{mklibname xxf86vm 1 -d -s}

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libXxf86vm.a

#-----------------------------------------------------------

%prep
%setup -q -n libXxf86vm-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXxf86vm.so.%{major}*

