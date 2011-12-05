%define tarball xf86-video-i128
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:   Xorg X11 i128 video driver
Name:      xorg-x11-drv-i128
Version:   1.3.3
Release:   1.1%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Source1:    i128.xinf

Patch0:	    i128-1.2.0-1600sw-range-hack.patch

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.4.99.1

Requires:  hwdata
Requires:  xorg-x11-server-Xorg >= 1.4.99.1

%description 
X.Org X11 i128 video driver.

%prep
%setup -q -n %{tarball}-%{version}

%patch0 -p1 -b .1600sw-hack

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/i128_drv.so
%{_datadir}/hwdata/videoaliases/i128.xinf
%{_mandir}/man4/i128.4*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.3.3-1.1
- Rebuilt for RHEL 6

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 1.3.3-1
- i128 1.3.3

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 1.3.2-1.1
- ABI bump

* Thu Jul 02 2009 Adam Jackson <ajax@redhat.com> 1.3.2-1
- i128 1.3.2

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 1.3.0-1
- Update to latest upstream release

* Mon Mar 03 2008 Adam Jackson <ajax@redhat.com> 1.2.1-3.20080303
- git snapshot for pciaccess support

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.1-2
- Autorebuild for GCC 4.3

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> 1.2.1-1
- xf86-video-i128 1.2.1

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 1.2.0-7
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.2.0-6
- Update Requires and BuildRequires.  Disown the module directories.  Add
  Requires: hwdata.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 1.2.0-5
- ExclusiveArch -> ExcludeArch

* Mon Aug 28 2006 Adam Jackson <ajackson@redhat.com> 1.2.0-4
- i128-1.2.0-1600sw-range-hack.patch: Also fill in maxPixClock and synthesize
  the appropriate modes when we don't get DDC.

* Wed Aug  2 2006 Adam Jackson <ajackson@redhat.com> 1.2.0-3
- i128-1.2.0-1600sw-range-hack.patch: Attempt to force the sync ranges
  correctly when we detect a 1600SW panel but don't get EDID info from it.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.2.0-2.1
- rebuild

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 1.2.0-2
- Rebuild for 7.1 ABI fix.

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 1.2.0-1
- Update to 1.2.0 from 7.1RC1.

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.1.0.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.1.0.5-1
- Updated xorg-x11-drv-i128 to version 1.1.0.5 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.1.0.4-1
- Updated xorg-x11-drv-i128 to version 1.1.0.4 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.1.0.2-1
- Updated xorg-x11-drv-i128 to version 1.1.0.2 from X11R7 RC2

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 1.1.0.1-1
- Updated xorg-x11-drv-i128 to version 1.1.0.1 from X11R7 RC1
- Fix *.la file removal.

* Mon Oct 3 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Limit "ExclusiveArch" to i386

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-0
- Initial spec file for i128 video driver generated automatically
  by my xorg-driverspecgen script.
