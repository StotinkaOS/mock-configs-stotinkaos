Summary:        Mock config files for the StotinkaOS
Name:           mock-configs-stotinkaos
Version:        1.0
Release:        1%{dist}
Group:          Development/Tools
License:        BSD
URL:            http://stotinkaos.net
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       mock

%description
%{summary}.

%prep
%setup -q

%build
#Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/mock
install -pm 0644 *.cfg $RPM_BUILD_ROOT%{_sysconfdir}/mock

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/mock/*.cfg

%changelog
* Sat Feb 27 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 1.0-1
- initial build
