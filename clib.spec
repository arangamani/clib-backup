Name:           clib
Version:        0.2.3
Release:        1%{?dist}
Summary:        A library for advanced C functions

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/arangamani/clib
Source:         https://github.com/downloads/arangamani/clib/clib-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  glibc
BuildRequires:  autoconf
BuildRequires:  libtool
Requires:  f2c

%description
clib is a development library which provides the end user with hashes,
arrays and other features that are very useful for programming in the
C programming language.

%package        devel
Summary:        Development files for the clib library
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
sh autogen.sh
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README INSTALL ChangeLog
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Sun Jan  8 2012 - Arangamanikkannan Manickam <arangamani.kannan@gmail.com> - 0.2.3-1
- Release for Fedora

* Wed Jul 29 2009 - Tonnerre Lombard <tonnerre.lombard@sygroup.ch> - 0.2.2-1
- Added destructors to the array API to match the hash API.

* Tue Jul 28 2009 - Tonnerre Lombard <tonnerre.lombard@sygroup.ch> - 0.2.1-1
- Added function to convert host:port strings to socket addresses for
  connect, bind etc.

* Tue Jul 21 2009 - Tonnerre Lombard <tonnerre.lombard@sygroup.ch> - 0.2.0-1
- Initial release for RedHat
