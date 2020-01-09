Name:           clutter-gst2
Version:        2.0.12
Release:        2%{?dist}
Summary:        GStreamer integration for Clutter

License:        LGPLv2+
URL:            http://www.clutter-project.org
Source0:        http://ftp.gnome.org/pub/GNOME/sources/clutter-gst/2.0/clutter-gst-%{version}.tar.xz
Patch1:         0001-video-sink-clear-buffer-in-flush.patch

BuildRequires:  clutter-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel

%description
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces.

Clutter GStreamer enables the use of GStreamer with Clutter.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces.

Clutter GStreamer enables the use of GStreamer with Clutter.

The %{name}-devel package contains libraries and header files for
developing applications that use clutter-gst API version 2.0.

%prep
%setup -q -n clutter-gst-%{version}
%patch1 -p1

%build
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Remove the documentation for now as it conflicts with the files in
# clutter-gst-devel. I'll work with upstream to fix this properly.
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING README
%{_libdir}/girepository-1.0/ClutterGst-2.0.typelib
%{_libdir}/gstreamer-1.0/libgstclutter.so
%{_libdir}/libclutter-gst-2.0.so.*

%files devel
%{_includedir}/clutter-gst-2.0/
%{_libdir}/libclutter-gst-2.0.so
%{_libdir}/pkgconfig/clutter-gst-2.0.pc
%{_datadir}/gir-1.0/ClutterGst-2.0.gir
#doc #{_datadir}/gtk-doc/

%changelog
* Tue May 19 2015 Wim Taymans <wtaymans@redhat.com> - 2.0.12-2
- Add patch to flush video sink, fixes errors in cheese
- Resolves: #1174515

* Thu Mar 19 2015 Richard Hughes <rhughes@redhat.com> - 2.0.12-1
- Update to 2.0.12
- Resolves: #1174515

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 2.0.4-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.0.4-2
- Mass rebuild 2013-12-27

* Sat May 25 2013 Kalev Lember <kalevlember@gmail.com> - 2.0.4-1
- Update to 2.0.4

* Tue Feb 26 2013 Kalev Lember <kalevlember@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 2.0.0-3
- Rebuilt for cogl soname bump

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.0-2
- Rebuild for new cogl

* Thu Jan 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.0-1
- Update to 2.0.0

* Tue Sep 25 2012 Matthias Clasen <mclasen@redhat.com> - 1.9.92-1
- Update to 1.9.92

* Wed Sep 19 2012 Kalev Lember <kalevlember@gmail.com> - 1.9.90-2
- Rebuilt with gstreamer1 0.11.99

* Wed Aug 29 2012 Kalev Lember <kalevlember@gmail.com> - 1.9.90-1
- Initial clutter-gst2 packaging, based on Fedora clutter-gst (#852778)
