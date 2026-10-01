Name:       sailfish-content-browser-verdanditeam
Version:    1.0
Release:    1
Summary:    Sailfish Browser VerdandiTeam content
License:    MPL v2.0
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Provides:   sailfish-content-browser
Conflicts:  sailfish-content-browser-default
Obsoletes:  sailfish-content-browser-default
Requires:   sailfish-content-graphics

%description
Sailfish Browser VerdandiTeam content

%prep
%setup -q

%install
install -d %{buildroot}%{_libdir}/mozembedlite/chrome/embedlite/content
install -m 0644 search-engines/*.xml %{buildroot}%{_libdir}/mozembedlite/chrome/embedlite/content/
install -d %{buildroot}%{_datadir}/sailfish-browser/default-content
install -m 0644 default-content/bookmarks.json %{buildroot}%{_datadir}/sailfish-browser/default-content/

%files
%{_libdir}/mozembedlite/chrome/embedlite/content/*.xml
%dir %{_datadir}/sailfish-browser/default-content
%{_datadir}/sailfish-browser/default-content/bookmarks.json
