%define major 1
%define libname %mklibname xxf86vm %{major}
%define devname %mklibname xxf86vm -d

Summary:	XFree86 Video Mode Extension Library
Name:		libxxf86vm
Version:	1.1.4
Release:	2
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86vm-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1
BuildRequires:	pkgconfig(xproto)

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
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -qn libXxf86vm-%{version}

%build
%configure \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXxf86vm.so.%{major}*

%files -n %{devname}
%{_libdir}/libXxf86vm.so
%{_libdir}/pkgconfig/xxf86vm.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/XF86VidMode*.*
%{_mandir}/man3/XF86VM.*

