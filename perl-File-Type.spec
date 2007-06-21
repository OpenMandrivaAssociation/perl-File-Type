%define module 	File-Type
%define version 0.22
%define release %mkrel 4

Summary:	Perl module to determine file type using magic
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PA/PMISON/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel 
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

%description
File::Type is a perl module that can be used to determine file type using magic.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/File/*
%{_mandir}/*/*


