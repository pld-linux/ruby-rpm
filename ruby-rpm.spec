Summary:	An interface to access RPM database for Ruby
Name:		ruby-rpm
Version:	1.2.3
Release:	0.1
License:	GPL
Group:		Development/Languages
URL:		http://rubyforge.org/projects/ruby-rpm/
Source0:	http://rubyforge.org/frs/download.php/26403/%{name}-%{version}.tgz
# Source0-md5:	a8be5d9582d964659802e0118f02e690
Patch1:		%{name}-doc.patch
Patch2:		%{name}-ia64.patch
Patch3:		%{name}-extconf-db46.patch
Patch4:		%{name}-compat.patch
BuildRequires:	db-devel
BuildRequires:	popt-devel >= 1.9.1
BuildRequires:	rpm-devel
BuildRequires:	ruby >= 1.8.6
BuildRequires:	ruby-devel >= 1.8.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby/RPM is an interface to access RPM database for Ruby.

%prep
%setup -q
%patch1 -p1
%ifarch ia64
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p1

%build
ruby install.rb config \
	--bin-dir=%{_bindir} \
	--rb-dir=%{ruby_sitelibdir} \
	--so-dir=%{ruby_sitearchdir} \
	--data-dir=%{_datadir}

ruby install.rb setup

%install
rm -rf $RPM_BUILD_ROOT
ruby install.rb config \
    --bin-dir=$RPM_BUILD_ROOT%{_bindir} \
    --rb-dir=$RPM_BUILD_ROOT%{ruby_sitelibdir} \
    --so-dir=$RPM_BUILD_ROOT%{ruby_sitearchdir} \
    --data-dir=$RPM_BUILD_ROOT%{_datadir}
ruby install.rb install

#install ext/rpm/ruby-rpm.h $RPM_BUILD_ROOT%{ruby_sitearchdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING ChangeLog doc
%{ruby_sitelibdir}/rpm.rb
%attr(755,root,root) %{ruby_sitearchdir}/rpmmodule.so
#%{ruby_sitearchdir}/ruby-rpm.h
