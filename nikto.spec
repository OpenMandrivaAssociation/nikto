%define _provides_exceptions perl(LW)

Summary:	Web Server and CGI Scanner
Name:		nikto
Version:	2.1.4
Release:	%mkrel 2
License:	GPL
Group:		Networking/Other
URL:		http://www.cirt.net/code/nikto.shtml
Source:		http://www.cirt.net/nikto/%{name}-%{version}.tar.bz2
Patch0:		nikto-2.1.1-fhs.patch
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%build

%install
rm -rf %{buildroot}


install -d -m 755 %{buildroot}%{_bindir}
install -m0755 nikto.pl %{buildroot}%{_bindir}/nikto

install -d -m 755 %{buildroot}%{_sysconfdir}
install -m0644 nikto.conf %{buildroot}%{_sysconfdir}

install -d %{buildroot}%{_datadir}/nikto/plugins
install -m0644 plugins/* %{buildroot}%{_datadir}/nikto/plugins
install -d %{buildroot}%{_datadir}/nikto/templates
install -m0644 templates/* %{buildroot}%{_datadir}/nikto/templates

install -d %{buildroot}%{_mandir}/man1
install -m0644 docs/nikto.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/CHANGES.txt docs/LICENSE.txt docs/nikto_manual.html docs/nikto.dtd
%config(noreplace) %{_sysconfdir}/nikto.conf
%{_datadir}/nikto
%{_bindir}/nikto
%{_mandir}/man1/nikto.1*


