%define upstream_name    Dist-Zilla-Plugin-OurPkgVersion
%define upstream_version 0.1.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    No line insertion and does Package version with our
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Dist::Zilla::Role::FileFinderUser)
BuildRequires: perl(Dist::Zilla::Role::FileMunger)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Moose)
BuildRequires: perl(PPI)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module was created as an alternative to the
Dist::Zilla::Plugin::PkgVersion manpage and uses some code from that
module. This module is designed to use a the more readable format 'our
$VERSION = $version;' as well as not change then number of lines of code in
your files, which will keep your repository more in sync with your CPAN
release. It also allows you slightly more freedom in how you specify your
version.

EXAMPLES
    in dist.ini

    	...
    	version = 0.01;
    	[OurPkgVersion]

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


