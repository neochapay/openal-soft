Name:       openal-soft
Summary:    A cross-platform 3D audio library
Version:    1.20.1
Release:    1
Group:      System/Libraries
License:    LGPLv2.1+
URL:        http://kcat.strangesoft.net/openal.html
Source0:    openal-soft-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  cmake

%description
Software implementation of the OpenAL API

%package devel
Summary:    Software implementation of the OpenAL API (development files)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name} = %{version}

%description devel
%{summary}.
OpenAL, the Open Audio Library, is a joint effort to create an open,
vendor-neutral, cross-platform API for interactive, primarily spatialized
audio. OpenAL's primary audience are application developers and desktop
users that rely on portable standards like OpenGL, for games and other
multimedia applications.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
%cmake .  \
    -DALSOFT_CONFIG=ON

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/libopenal.so.*
%{_datadir}/openal

%files devel
%defattr(-,root,root,-)
%{_includedir}/AL/*.h
%{_libdir}/*.so
%{_libdir}/cmake/OpenAL/*.cmake
%{_libdir}/pkgconfig/*.pc
