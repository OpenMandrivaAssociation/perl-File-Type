%define upstream_name 	 File-Type
%define upstream_version 0.22

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl module to determine file type using magic
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PA/PMISON/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
File::Type is a perl module that can be used to determine file type using
magic.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/File/*
%{_mandir}/*/*

%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.0
+ Revision: 406007
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.22-6mdv2009.0
+ Revision: 257038
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 0.22-4mdv2008.1
+ Revision: 166676
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jun 21 2007 Michael Scherer <misc@mandriva.org> 0.22-4mdv2008.0
+ Revision: 41992
- rebuild


* Thu Oct 06 2005 Michael Scherer <misc@mandriva.org> 0.22-2mdk
- mkrel
- policy compliance

* Tue Oct 05 2004 Michael Scherer <misc@mandrake.org> 0.22-1mdk 
- First Mandrakelinux package

