Summary:	KEasyCD - KDE CD recording frontend
Name:		keasycd
Version:	0.1.8
Release:	1
Group:		X11/KDE/Applications
Group(de):	X11/KDE/Applikationen
Group(pl):	X11/KDE/Aplikacje
License:	GPL
Vendor:		Marcel Borreda <marcel.borreda@post.rwth-aachen.de>
Source0:	%{name}-%{version}.tar.gz
URL:		http://
BuildRequires:	qt-devel >= 1.30
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
KEasyCD is a CD recording frontend for cdrecord, cdda2wav, cdparanoia,
and mkisofs.

%prep
%setup -q

%build
CXXFLAGS="%{rpmcflags}" CFLAGS="%{rpmcflags}" ./configure \
	--prefix=%{_prefix} --with-install-root=$RPM_BUILD_ROOT
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keasycd
%{_applnkdir}/Applications/keasycd.kdelnk
%{_docdir}/HTML/en/keasycd/*
%{_datadir}/icons/*
