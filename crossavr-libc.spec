Summary:	AVR libc
Summary(pl):	libc na AVR
Name:		crossavr-libc
Version:	1.2.0
Release:	1
Epoch:		1
License:	Modified BSD (see included LICENSE)
Group:		Development/Tools
Source0:	http://savannah.nongnu.org/download/avr-libc/avr-libc-%{version}.tar.bz2
# Source0-md5:	a3b4518993616c3f494223886656f19d
Source1:	http://savannah.nongnu.org/download/avr-libc/avr-libc-user-manual-%{version}.tar.bz2
# Source1-md5:	c30a5af0ca08b6dd10eca63d5cd2ebbb
URL:		http://www.nongnu.org/avr-libc/
BuildRequires:	crossavr-binutils >= 2.14
BuildRequires:	crossavr-gcc >= 3.3
Requires:	crossavr-gcc >= 3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		avr
%define		arch		%{_prefix}/%{target}
%define		no_install_post_strip	1

%description
Contains the standard C library for Atmel AVR microcontrollers.

%description -l pl
Pakiet zawiera standardow± bibliotekê C dla mikrokontrolerów Atmel
AVR.

%prep
%setup -q -n avr-libc-%{version} -a1

%build
CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" \
CONFIG_SHELL="/bin/bash" \
PREFIX=%{arch}
./doconf
./domake

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} -C build install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

cp -rf doc/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%if 0%{!?debug:1}
%{target}-strip -g $RPM_BUILD_ROOT%{arch}/lib/*.[oa] \
	$RPM_BUILD_ROOT%{arch}/lib/avr?/*.[oa]
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc avr-libc-user-manual-%{version}/ ChangeLog LICENSE README NEWS
%attr(755,root,root) %{_bindir}/*
%dir %{arch}/include
%{arch}/include/*.h
%dir %{arch}/include/avr
%{arch}/include/avr/*.h
%{arch}/lib/*.[oa]
%dir %{arch}/lib/avr?
%{arch}/lib/avr?/*.[oa]
%{_examplesdir}/%{name}-%{version}
