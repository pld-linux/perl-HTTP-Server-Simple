#
# Conditional build:
%bcond_with	tests	# unit tests
#
%define	pdir	HTTP
%define	pnam	Server-Simple
Summary:	HTTP::Server::Simple - Lightweight HTTP server
Summary(pl.UTF-8):	HTTP::Server::Simple - lekki serwer HTTP
Name:		perl-HTTP-Server-Simple
Version:	0.52
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/B/BP/BPS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1e23935491d9a2a8b0ba636462255656
URL:		https://metacpan.org/dist/HTTP-Server-Simple
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple standalone HTTP server. By default, it doesn't thread
or fork. It does, however, act as a simple frontend which can be used
to build a standalone web-based application or turn a CGI into one.
It's possible to use Net::Server to get threading, forking, preforking
and so on. Autrijus Tang wrote the functionality and owes docs for
that.

%description -l pl.UTF-8
HTTP::Server::Simple jest prostym, samodzielnym serwerem HTTP.
Domyślnie nie obsługuje on wątków i podprocesów, jednakże może
byc użyty jako frontend do budowy samodzielnej aplikacji WWW lub jako
CGI. Możliwe jest użycie modułu Net::Server do obsługi wątków,
podprocesów itp. z wykorzystaniem kodu stworzonego przez Autrijusa
Tanga.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTTP/Server
%{_mandir}/man3/HTTP::Server::*.3pm*
