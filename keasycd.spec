%define name keasycd
%define version 0.1.8
%define release 1
%define prefix /opt/kde

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: KEasyCD - KDE CD recording frontend
Name: %{name}
Version: %{version}
Release: %{release}
Group: X11/KDE/Apps
Copyright: GPL
Vendor: Marcel Borreda <marcel.borreda@post.rwth-aachen.de>
Packager: Troy Engel <tengel@sonic.net>
Source: %{name}-%{version}.tar.gz
URL: http://
Requires: qt >= 1.30 kdelibs
BuildRoot: /tmp/build-%{name}-%{version}

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
rm -rf %{builddir}

%files
%defattr(-,root,root)
%{prefix}/bin/keasycd
%{prefix}/share/applnk/Applications/keasycd.kdelnk
%{prefix}/share/doc/HTML/en/keasycd/*
%{prefix}/share/icons/*
