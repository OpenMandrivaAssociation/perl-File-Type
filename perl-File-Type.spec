%define upstream_name 	 File-Type
%define upstream_version 0.22

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl module to determine file type using magic
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PA/PMISON/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
File::Type is a perl module that can be used to determine file type using
magic.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
