%define		rel		1
%define		subver	rc9
Summary:	Network Package Audit and Capture
Name:		ipaudit
Version:	1.0
Release:	0.%{subver}.%{rel}
License:	GPL v2
Group:		Networking
Source0:	http://downloads.sourceforge.net/ipaudit/%{name}-%{version}%{subver}.tar.gz
# Source0-md5:	3f0fe696cac8ff29651ec7aecd897536
URL:		http://ipaudit.sourceforge.net/
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A neat packet logging program and auditor. Provides dump capability
and various levels of logging.

%prep
%setup -q -n %{name}-%{version}%{subver}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL README
%attr(755,root,root) %{_bindir}/total
%attr(755,root,root) %{_sbindir}/ipaudit
%attr(755,root,root) %{_sbindir}/ipstrings
%{_mandir}/man8/ipaudit.8.*
%{_mandir}/man8/ipstrings.8.*
%{_mandir}/man1/total.1.*
