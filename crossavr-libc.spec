Summary:	AVR libc
Summary(pl):	libc na AVR
Name:		crossavr-libc
Version:	1.0.2
Release:	2
Epoch:		1
License:	Modified BSD (see included LICENSE)
Group:		Development/Tools
Source0:	http://savannah.nongnu.org/download/avr-libc/avr-libc-%{version}.tar.gz
# Source0-md5:	7ed0af0f978c0b62ee0e07d3af58eeee
Source1:	http://savannah.nongnu.org/download/avr-libc/avr-libc-user-manual.tar.bz2
# Source1-md5:	3ab9c2da3203b267d5c19ad9af92e089
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

%{__make} -C build install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%if 0%{!?debug:1}
%{target}-strip -g $RPM_BUILD_ROOT%{arch}/lib/*.[oa] \
	$RPM_BUILD_ROOT%{arch}/lib/avr?/*.[oa]
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html avr-libc-user-manual/ LICENSE README NEWS
%dir %{arch}/include
%{arch}/include/*.h
%dir %{arch}/include/avr
%{arch}/include/avr/*.h
%{arch}/lib/*.[oa]
%dir %{arch}/lib/avr?
%{arch}/lib/avr?/*.[oa]
