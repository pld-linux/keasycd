Summary:	KEasyCD - KDE CD recording frontend
Summary(pl):	KEasyCD - frontend KDE do nagrywania CD
Name:		keasycd
Version:	0.1.8
Release:	1
License:	GPL
Vendor:		Marcel Borreda <marcel.borreda@post.rwth-aachen.de>
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/unstable/apps/KDE1.x/multimedia/cdrom/%{name}-%{version}.tar.gz
BuildRequires:	qt-devel >= 1.30
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
KEasyCD is a CD recording frontend for cdrecord, cdda2wav, cdparanoia,
and mkisofs.

%description -l pl
KEasyCD jest s³u¿±cym do nagrywania CD frontendem KDE do programów
cdrecord, cdda2wav, cdparanoia i mkisofs.

%prep
%setup -q -n %{name}

%build
CXXFLAGS="%{rpmcflags}"
CFLAGS="%{rpmcflags} -I%{_includedir}/qt"

%configure2_13 \
	--prefix=%{_prefix} \
	--with-qt-dir=%{_includedir}/qt \
	--with-qt-includes=%{_includedir}/qt \
	--with-install-root=$RPM_BUILD_ROOT

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
