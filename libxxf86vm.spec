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

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	x11-proto-devel >= 7.5
BuildRequires:	x11-util-macros >= 1.0.1

%description
XFree86 Video Mode Extension Library

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libname}
XFree86 Video Mode Extension Library

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	libxorg-x11-devel < 7.0
Conflicts:	x11-proto-devel < 7.5
Obsoletes:	%{_lib}xxf86vm1-devel < 1.1.2
Obsoletes:	%{_lib}xxf86vm-static-devel < 1.1.2

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


%changelog
* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.2-1
+ Revision: 783812
- version update 1.1.2

* Wed Dec 28 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.1-3
+ Revision: 745844
- forgot a piece
- rebuild
- disabled static build
- removed .la files
- cleaned up spec

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2
+ Revision: 660308
- mass rebuild

* Sat Oct 30 2010 Thierry Vignaud <tv@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 590424
- new release

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.0-1mdv2010.1
+ Revision: 464052
- New version: 1.1.0

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-4mdv2010.0
+ Revision: 425975
- rebuild

* Sun Nov 09 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-3mdv2009.1
+ Revision: 301210
- rebuild for new xcb

* Fri Nov 07 2008 Olivier Blin <blino@mandriva.org> 1.0.2-2mdv2009.1
+ Revision: 300405
- rebuild for new xcb

* Wed Jul 16 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.0.2-1mdv2009.0
+ Revision: 236607
- Update to version 1.0.2

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2009.0
+ Revision: 223092
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Tue Jan 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-3mdv2008.1
+ Revision: 152768
- Update BuildRequires and rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-3mdv2008.0
+ Revision: 68819
- rebuild for 2008
- new devel policy
- spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages extension

