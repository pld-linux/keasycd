Summary:	KEasyCD - KDE CD recording frontend
Name:		keasycd
Version:	0.1.8
Release:	1
Group:		X11/KDE/Applications
Copyright:	GPL
Vendor:		Marcel Borreda <marcel.borreda@post.rwth-aachen.de>
Source:		%{name}-%{version}.tar.gz
URL:		http://
BuildPrereq:	qt-devel >= 1.30
BuildPrereq:	kdelibs-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
KEasyCD is a CD recording frontend for cdrecord, cdda2wav, cdparanoia,
and mkisofs.

%prep
%setup

%build
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=%{prefix} --with-install-root=$RPM_BUILD_ROOT
make

%install
rm -rf $RPM_BUILD_ROOT
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{prefix}/bin/keasycd
%{prefix}/share/applnk/Applications/keasycd.kdelnk
%{prefix}/share/doc/HTML/en/keasycd/*
%{prefix}/share/icons/*
