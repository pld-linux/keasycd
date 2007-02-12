Summary:	KEasyCD - KDE CD recording frontend
Summary(pl.UTF-8):   KEasyCD - frontend KDE do nagrywania CD
Name:		keasycd
Version:	0.1.9
Release:	1
License:	GPL
Vendor:		Marcel Borreda <marcel.borreda@post.rwth-aachen.de>
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/unstable/apps/KDE1.x/multimedia/cdrom/%{name}-%{version}.tar.gz
Source0:	http://ftp.kde.com/Multimedia/Audio/Burners_Rippers/KEasyCD/%{name}-%{version}.tar.gz
# Source0-md5:	2d4a211e737379f91245d20fb6158d8c
BuildRequires:	kdelibs-devel >= 1.1
BuildRequires:	kdelibs-devel < 2.0
BuildRequires:	qt-devel >= 1.30
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%description
KEasyCD is a CD recording frontend for cdrecord, cdda2wav, cdparanoia,
and mkisofs.

%description -l pl.UTF-8
KEasyCD jest służącym do nagrywania CD frontendem KDE do programów
cdrecord, cdda2wav, cdparanoia i mkisofs.

%prep
%setup -q -n %{name}

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure2_13 \
	--with-qt-dir=/usr/include/qt \
	--with-qt-includes=/usr/include/qt \
	--with-install-root=$RPM_BUILD_ROOT

%{__make} \
	CXXFLAGS="%{rpmcflags} -I/usr/include/qt"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keasycd
%{_applnkdir}/Applications/keasycd.kdelnk
%{_pixmapsdir}/*
