Name:           libchromaprint
Version:        1.3.2
Release:        1%{?dist}
Summary:        Library implementing the AcoustID fingerprinting

License:        LGPL2.1+
URL:            https://acoustid.org/chromaprint
Source0:        https://bitbucket.org/acoustid/chromaprint/downloads/chromaprint-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fftw-devel >= 3

%description
Chromaprint library is the core component of the AcoustID project. It's a
client-side library that implements a custom algorithm for extracting
fingerprints from raw audio sources.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n chromaprint-%{version}


%build
mkdir build
pushd build
%{cmake} ..
make %{?_smp_mflags}
popd


%install
rm -rf %{buildroot}
pushd build
%make_install
popd


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc
%{_libdir}/*.so.*

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Wed Aug 10 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.3.2-1
- Public release
