#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Parse
%define		pnam	DebControl
%include	/usr/lib/rpm/macros.perl
Summary:	Easy OO parsing of debian control-like files
Name:		perl-Parse-DebControl
Version:	2.005
Release:	1
License:	GPL+ or Artistic
Group:		Applications/File
Source0:	http://search.cpan.org/CPAN/authors/id/J/JA/JAYBONCI/Parse-DebControl-%{version}.tar.gz
# Source0-md5:	4fbf2e0b28a471a5e94394615303daf6
URL:		http://search.cpan.org/dist/Parse-DebControl/
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-base
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(strict)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy OO parsing of debian control-like files.

%prep
%setup -q -n Parse-DebControl-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

# Remove empty directory tree
rm -r $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{perl_vendorlib}/Parse/DebControl.pm
%{_mandir}/man3/Parse::DebControl.3pm*
