%define _provides_exceptions perl(LW)

Summary:	Nikto  - Web Server and CGI Scanner
Name:		nikto
Version:	1.35
Release:	%mkrel 5
License:	GPL
Group:		Networking/Other
URL:		http://www.cirt.net/code/nikto.shtml
Source:		http://www.cirt.net/nikto/%{name}-%{version}.tar.bz2
Patch0:		nikto-1.35.mdv_conf.diff
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Nikto is an Open Source (GPL) web server scanner which performs
comprehensive tests against web servers for multiple items,
including over 3200 potentially dangerous files/CGIs, versions on
over 625 servers, and version specific problems on over 230
servers. Scan items and plugins are frequently updated and can be
automatically updated (if desired).

%prep

%setup -q
%patch0 -p1

chmod 644 docs/*

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/nikto/plugins
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man1

install -m0740 nikto.pl %{buildroot}%{_sbindir}/nikto
install -m0644 config.txt %{buildroot}%{_sysconfdir}/nikto/nikto.conf
install -m0644 versions.txt %{buildroot}%{_sysconfdir}/nikto/
install -m0644 plugins/* %{buildroot}%{_sysconfdir}/nikto/plugins/
install -m0644 docs/nikto-1.34.man %{buildroot}%{_mandir}/man1/nikto.1
ln -s %{_docdir}/%{name}-%{version} %{buildroot}%{_sysconfdir}/nikto/docs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/CHANGES.txt docs/LICENSE.txt docs/nikto_usage.html docs/nikto_usage.txt docs/README_plugins.txt
%attr(0755,root,root) %dir %{_sysconfdir}/nikto
%attr(0755,root,root) %dir %{_sysconfdir}/nikto/plugins
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nikto/nikto.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nikto/versions.txt
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nikto/plugins/*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nikto/docs
%attr(0740,root,root) %{_sbindir}/nikto
%attr(0644,root,root) %{_mandir}/man1/nikto.1*


