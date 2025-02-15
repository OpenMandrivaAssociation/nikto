%define __noautoprov 'perl\\(.*\\)'

Summary:	Web Server and CGI Scanner
Name:		nikto
Version:	2.5.0
Release:	1
License:	GPLv2+
Group:		Monitoring
Url:		https://github.com/sullo/nikto
Source0:	https://github.com/sullo/nikto/archive/refs/tags/%{version}.tar.gz
Patch0:		nikto-2.1.5-fhs.patch
BuildArch:	noarch

%description
Nikto is a web server scanner which performs comprehensive tests against web
servers for multiple items, including over 3200 potentially dangerous
files/CGIs, versions on over 625 servers, and version specific problems on over
230 servers. Scan items and plugins are frequently updated and can be
automatically updated (if desired).

%files
%config(noreplace) %{_sysconfdir}/nikto.conf
%{_datadir}/nikto
%{_bindir}/nikto
%{_mandir}/man1/nikto.1*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m0755 program/nikto.pl %{buildroot}%{_bindir}/nikto

install -d -m 755 %{buildroot}%{_sysconfdir}
install -m0644 program/nikto.conf.default %{buildroot}%{_sysconfdir}/nikto.conf

install -d -m 755 %{buildroot}%{_datadir}/nikto
cp -pr program/plugins %{buildroot}%{_datadir}/nikto
cp -pr program/templates %{buildroot}%{_datadir}/nikto
cp -pr program/databases %{buildroot}%{_datadir}/nikto

install -d %{buildroot}%{_mandir}/man1
install -m0644 documentation/nikto.1 %{buildroot}%{_mandir}/man1
