# libxxf86vm is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 1
%define libname %mklibname xxf86vm %{major}
%define devname %mklibname xxf86vm -d
%if %{with compat32}
%define lib32name libxxf86vm%{major}
%define dev32name libxxf86vm-devel
%endif

%global optflags %{optflags} -O3

Summary:	XFree86 Video Mode Extension Library
Name:		libxxf86vm
Version:	1.1.5
Release:	2
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86vm-%{version}.tar.xz
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1
BuildRequires:	pkgconfig(xproto)
%if %{with compat32}
BuildRequires:	libc6
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXext)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

%description
XFree86 Video Mode Extension Library.

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		Development/X11

%description -n %{libname}
XFree86 Video Mode Extension Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	Shared libraries for %{name} (32-bit)
Group:		Development/X11

%description -n %{lib32name}
XFree86 Video Mode Extension Library.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{lib32name} = %{version}
Requires:	%{devname} = %{version}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXxf86vm-%{version} -p1
export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXxf86vm.so.%{major}*

%files -n %{devname}
%{_libdir}/libXxf86vm.so
%{_libdir}/pkgconfig/xxf86vm.pc
%{_includedir}/X11/extensions/*.h
%doc %{_mandir}/man3/XF86VidMode*.*
%doc %{_mandir}/man3/XF86VM.*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXxf86vm.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXxf86vm.so
%{_prefix}/lib/pkgconfig/xxf86vm.pc
%endif
