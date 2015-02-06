%define __noautoprov 'perl\\(.*\\)'

Summary:	Web Server and CGI Scanner
Name:		nikto
Version:	2.1.5
Release:	2
License:	GPLv2+
Group:		Monitoring
Url:		http://www.cirt.net/code/nikto.shtml
Source0:	http://www.cirt.net/nikto/%{name}-%{version}.tar.bz2
Patch0:		nikto-2.1.5-fhs.patch
Patch1:		nikto-2.1.5-fix-path-in-man.diff
BuildArch:	noarch

%description
Nikto is a web server scanner which performs comprehensive tests against web
servers for multiple items, including over 3200 potentially dangerous
files/CGIs, versions on over 625 servers, and version specific problems on over
230 servers. Scan items and plugins are frequently updated and can be
automatically updated (if desired).

%files
%doc docs/CHANGES.txt docs/LICENSE.txt docs/nikto_manual.html docs/nikto.dtd
%config(noreplace) %{_sysconfdir}/nikto.conf
%{_datadir}/nikto
%{_bindir}/nikto
%{_mandir}/man1/nikto.1*

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m0755 nikto.pl %{buildroot}%{_bindir}/nikto

install -d -m 755 %{buildroot}%{_sysconfdir}
install -m0644 nikto.conf %{buildroot}%{_sysconfdir}

install -d -m 755 %{buildroot}%{_datadir}/nikto
cp -pr plugins %{buildroot}%{_datadir}/nikto
cp -pr templates %{buildroot}%{_datadir}/nikto
cp -pr databases %{buildroot}%{_datadir}/nikto

install -d %{buildroot}%{_mandir}/man1
install -m0644 docs/nikto.1 %{buildroot}%{_mandir}/man1

