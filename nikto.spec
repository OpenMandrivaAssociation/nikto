%define _provides_exceptions perl(LW)

Summary:	Web Server and CGI Scanner
Name:		nikto
Version:	2.1.4
Release:	%mkrel 3
License:	GPL
Group:		Monitoring
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




%changelog
* Thu Jul 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.4-3mdv2011
+ Revision: 689086
- switch group to monitoring, as other security-related tools

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.4-2
+ Revision: 674553
- fix  configuration file location

* Mon Feb 28 2011 Lonyai Gergely <aleph@mandriva.org> 2.1.4-1
+ Revision: 641049
- 2.1.4

* Fri Nov 19 2010 Lonyai Gergely <aleph@mandriva.org> 2.1.3-1mdv2011.0
+ Revision: 599045
- 2.1.3

* Tue Apr 20 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.1-1mdv2010.1
+ Revision: 536971
- new version
- install plugins as data, not configuration
- install binary under %%{_bindir}, as root usage is not mandatory
- use standard exec permissions

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.35-5mdv2010.0
+ Revision: 430173
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.35-4mdv2009.0
+ Revision: 253954
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.35-2mdv2008.1
+ Revision: 136631
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 01 2006 Oden Eriksson <oeriksson@mandriva.com> 1.35-2mdv2007.0
+ Revision: 89746
- Import nikto

* Sun Nov 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.35-2mdk
- added a softlink to make nikto -update work

* Wed Nov 16 2005 Oden Eriksson <oeriksson@mandriva.com> 1.35-1mdk
- initial Mandriva package

