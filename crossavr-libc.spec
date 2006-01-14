Summary:	AVR libc
Summary(pl):	libc na AVR
Name:		crossavr-libc
Version:	1.4.2
Release:	1
Epoch:		1
License:	Modified BSD (see included LICENSE)
Group:		Development/Tools
Source0:	http://savannah.nongnu.org/download/avr-libc/avr-libc-%{version}.tar.bz2
# Source0-md5:	d4cb171169cabda4889ba6f6a58f1fa8
Source1:	http://savannah.nongnu.org/download/avr-libc/avr-libc-user-manual-%{version}.tar.bz2
# Source1-md5:	7302c9cc8f315ab6b6ce1d1c57bd29bf
Source2:	http://savannah.nongnu.org/download/avr-libc/avr-libc-manpages-%{version}.tar.bz2
# Source2-md5:	3837a83f7087280052d3207e2397c121
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
%setup -q -n avr-libc-%{version} -a1 -a2

%build
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcflags}" \
./configure \
	--prefix=%{_prefix} \
	--build=%{_target_platform} \
	--host=%{target} 
%{__make} \
	DOC_INST_DIR="%{_datadir}/%{name}-%{version}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

cp -rf doc/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -rf man $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

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
%dir %{arch}/include/compat
%{arch}/include/compat/*.h
%dir %{arch}/include/util
%{arch}/include/util/*.h
%{arch}/lib/*.[oa]
%dir %{arch}/lib/avr?
%{arch}/lib/avr?/*.[oa]
%{_datadir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}
