Summary:	AVR libc
Summary(pl):	libc na AVR
Name:		crossavr-libc
Version:	20020203
Release:	1
License:	Public Domain
Group:		Development/Tools
Source0:	http://savannah.nongnu.org/download/avr-libc/avr-libc-%{version}.tar.gz
# Source0-md5:	fb80cdba885f5ed0f62422393062255f
URL:		http://www.nongnu.org/avr-libc/
BuildRequires:	crossavr-binutils
BuildRequires:	crossavr-gcc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		avr
%define		arch		%{_prefix}/%{target}

%description
Contains the standard C library for Atmel AVR microcontrollers.

%description -l pl
Pakiet zawiera standardow� bibliotek� C dla mikrokontroler�w Atmel AVR.

%prep
%setup -q -n avr-libc-%{version}

%build
CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" \
CONFIG_SHELL="/bin/bash" \
PREFIX=%{arch}
./doconf
./domake

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

cd build
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html
%dir %{arch}/include
%{arch}/include/*.h
%dir %{arch}/lib
%{arch}/lib/*.[oa]
%dir %{arch}/lib/avr?
%{arch}/lib/avr?/*.[oa]
