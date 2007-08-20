%define libxxf86vm %mklibname xxf86vm 1
Name: libxxf86vm
Summary:  XFree86 Video Mode Extension Library
Version: 1.0.1
Release: %mkrel 2
Group: Development/X11
License: MIT
Packager: Gustavo Pichorim Boiko <boiko@mandriva.com>
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXxf86vm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
XFree86 Video Mode Extension Library

#-----------------------------------------------------------

%package -n %{libxxf86vm}
Summary: Development files for %{name}
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxxf86vm}
XFree86 Video Mode Extension Library

#-----------------------------------------------------------

%package -n %{libxxf86vm}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxxf86vm} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxxf86vm-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxxf86vm}-devel
Development files for %{name}

%files -n %{libxxf86vm}-devel
%defattr(-,root,root)
%{_libdir}/libXxf86vm.so
%{_libdir}/libXxf86vm.la
%{_libdir}/pkgconfig/xxf86vm.pc
%{_mandir}/man3/XF86VidMode*.*
%{_mandir}/man3/XF86VM.*

#-----------------------------------------------------------

%package -n %{libxxf86vm}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxxf86vm}-devel = %{version}
Provides: libxxf86vm-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxxf86vm}-static-devel
Static development files for %{name}

%files -n %{libxxf86vm}-static-devel
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxxf86vm}
%defattr(-,root,root)
%{_libdir}/libXxf86vm.so.1
%{_libdir}/libXxf86vm.so.1.0.0


