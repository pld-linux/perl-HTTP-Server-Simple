#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTP
%define	pnam	Server-Simple
Summary:	HTTP::Server::Simple - Lightweight HTTP server
Summary(pl.UTF-8):	HTTP::Server::Simple - Lekki serwer HTTP
Name:		perl-HTTP-Server-Simple
Version:	0.42
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JE/JESSE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c31d15138498b063642882d03338f5f6
URL:		http://search.cpan.org/dist/HTTP-Server-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{_mandir}/man3/*
