%define realname NoCatSplash

Summary:	NoCatSplash is a Open Public Network Gateway Daemon
Name:		nocatsplash
Version:	0.93pre2
Release:	%mkrel 2
License:        GPL
Group:		Networking/Remote access
BuildRequires:	glib-devel
Source0:	http://nocat.net/download/%{realname}/%{realname}-%{version}.tar.bz2
Source1:	NoCatSplashSetup.txt
Source2:	%{realname}-firewall-scripts.tar.bz2
Patch0:		NoCatSplash-mdv-greeting.patch
URL:            http://nocat.net/wiki/index.cgi?NoCatSplash
Requires:	iptables

%description
NoCatSplash is a Open Public Network Gateway Daemon.  It performs as a
[captive/open/active] portal.  When run on a gateway/router on a network,
all web requests are redirected until the client either logs in or clicks
"I Accept" to an AUP. The gateway daemon then changes the firewall rules
on the gateway to pass traffic for that client (based on IP address and
MAC address).

%prep

%setup -q -a2 -n %{realname}-%{version}
%patch0 -p1
cp %SOURCE1 .

%build
%configure --with-firewall=iptables
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO NoCatSplashSetup.txt
%dir %{_datadir}/nocat
%{_datadir}/nocat/*
%dir %{_libdir}/nocat
%{_libdir}/nocat/*
%{_sbindir}/splashd
%config(noreplace) %{_sysconfdir}/nocat.conf
%{_mandir}/man5/*
%{_mandir}/man8/*


