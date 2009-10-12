Summary:	AVR libc
Summary(pl.UTF-8):	libc na AVR
Name:		crossavr-libc
Version:	1.6.7
Release:	1
Epoch:		1
License:	Modified BSD (see included LICENSE)
Group:		Development/Tools
Patch0:		%{name}-builtins.patch
Patch1:		%{name}-dwarf2.patch
Source0:	http://download.savannah.gnu.org/releases/avr-libc/avr-libc-%{version}.tar.bz2
# Source0-md5:	1ccf8078e583d527392f079082f816b0
Source1:	http://download.savannah.gnu.org/releases/avr-libc/avr-libc-user-manual-%{version}.tar.bz2
# Source1-md5:	d5f410aa9598d2f51afe9c3002238aa7
Source2:	http://download.savannah.gnu.org/releases/avr-libc/avr-libc-manpages-%{version}.tar.bz2
# Source2-md5:	26f6cf3f57fa2ab4d492eb0d0d72b886
URL:		http://www.nongnu.org/avr-libc/
BuildRequires:	crossavr-binutils >= 2.14
BuildRequires:	crossavr-gcc >= 1:3.3
Requires:	crossavr-gcc >= 1:3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		avr
%define		arch		%{_prefix}/%{target}

%define		__strip		%{target}-strip

%description
Contains the standard C library for Atmel AVR microcontrollers.

%description -l pl.UTF-8
Pakiet zawiera standardową bibliotekę C dla mikrokontrolerów Atmel
AVR.

%prep
%setup -q -n avr-libc-%{version} -a1 -a2
%patch0 -p0
%patch1 -p0

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
rm -rf $RPM_BUILD_ROOT%{_docdir}/avr-libc-%{version}/examples

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
%dir %{arch}/lib/avr*
%{arch}/lib/avr*/*.[oa]
%{_datadir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}
