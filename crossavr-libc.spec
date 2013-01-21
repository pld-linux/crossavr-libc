Summary:	AVR libc
Summary(pl.UTF-8):	libc na AVR
Name:		crossavr-libc
Version:	1.8.0
Release:	3
Epoch:		1
License:	Modified BSD (see included LICENSE)
Group:		Development/Tools
Patch0:		%{name}-builtins.patch
# Patches 1xx are taken form Atmel official AVR8-GNU toolchain version 3.4.1.830
Patch100:	300-avr-libc-bug15254.patch
Patch101:	301-avr-libc-bugavrtc-436.patch
Patch102:	302-avr-libc-bug-avrtc-441.patch
Patch103:	303-avr-libc-avrtc536.patch
Patch104:	304-avr-libc-avrtc-608.patch
Patch105:	400-avr-libc-public-devices.patch
Patch106:	401-avr-libc-atmega_rfr2.patch
Patch107:	402-avr-libc-atxmega32_16_8e5.patch
Patch108:	403-avr-libc-powerh-doc.patch
Patch109:	500-avr-libc-bug12507.patch
Patch110:	501-avr-libc-bug12584.patch
Patch111:	502-avr-libc-bug12838.patch
Patch112:	503-avr-libc-headersio.patch
Patch113:	504-avr-libc-bugavrtc-448.patch
Patch114:	505-avr-libc-avrtc-519.patch
Patch115:	506-avr-libc-optimize_dox.patch
Patch116:	507-avr-libc-avrtc570.patch
Patch117:	508-avr-libc-avrtc446.patch
Patch118:	999-avr-libc-new-headers.patch
Source0:	http://download.savannah.gnu.org/releases/avr-libc/avr-libc-%{version}.tar.bz2
# Source0-md5:	54c71798f24c96bab206be098062344f
Source1:	http://download.savannah.gnu.org/releases/avr-libc/avr-libc-user-manual-%{version}.tar.bz2
# Source1-md5:	d8a02a987cc0ea447348e0b6a08ab679
Source2:	http://download.savannah.gnu.org/releases/avr-libc/avr-libc-manpages-%{version}.tar.bz2
# Source2-md5:	35af895d775015731b77d027a9e07cca
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
%patch100 -p0
%patch101 -p0
%patch102 -p0
%patch103 -p0
%patch104 -p0
%patch105 -p0
%patch106 -p0
%patch107 -p0
%patch108 -p0
%patch109 -p0
%patch110 -p0
%patch111 -p0
%patch112 -p0
%patch113 -p0
%patch114 -p0
%patch115 -p0
%patch116 -p0
%patch117 -p0
%patch118 -p1

%build
./bootstrap

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
