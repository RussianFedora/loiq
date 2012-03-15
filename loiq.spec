Summary:            Low Orbit Ion Cannon in Qt
Name:               loiq
Version:            0.3.1a
Release:            3%{?dist}
Summary:            Low Orbit Ion Cannon in Qt
Summary(ru):        Low Orbit Ion Cannon на Qt

Source:             http://downloads.sourceforge.net/project/loiq/%{name}-%{version}.tar.bz2
Source1:            loiq.desktop
URL:                http://loiq.sourceforge.net/
Group:              Applications/Internet
License:            GPLv3

%if 0%{?fedora} >= 15 && 0%{?rhel} >= 7
BuildRequires:  qt-devel
%else
BuildRequires:  qt4-devel
%endif


%description
LOIQ stands for Low Orbit Ion Cannon in Qt. It is an attempt to port the famous
public-domain server stress-testing tool from C#/.Net to C++/Qt4, thus making it
available for the vast community of GNU/Linux users, as well as for the rest of
us *NIXoids.

%description -l ru
LOIQ это аналог Low Orbit Ion Cannon на Qt. Это попытка портировать известное
открытое средства для стресс-тестирования серверов с C#/.Net на C++/Qt4, и
сделать его доступным для широкого сообщества пользователей GNU/Linux, а
так же для всех *NIXoid'дов.


%prep
%setup -q
qmake-qt4 -o Makefile loiq.pro
make clean


%build
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make INSTALL_ROOT=%{buildroot} INSTALL="install -p" CP="cp -p" install
install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

strip %{buildroot}%{_bindir}/%{name}


%clean
rm -rf %{buildroot}


%files 
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Mon Feb 06 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.1a-3.R
- added conditions to build for EL6

* Tue Nov 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.1a-2.R
- Added description in russian language

* Fri Jul  8 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.1a-1.R
- initial build
