%define upstream_name    Dist-Zilla-Plugin-OurPkgVersion
%define upstream_version 0.005001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	No line insertion and does Package version with our

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Test::Version)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Dist::Zilla::Role::FileFinderUser)
BuildRequires:	perl(Dist::Zilla::Role::FileMunger)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Moose)
BuildRequires:	perl(PPI)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


