%define pkgname rpm
Summary:	An interface to access RPM database for Ruby
Name:		ruby-%{pkgname}
Version:	1.3.1
Release:	6
License:	GPL v2
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/ruby-rpm-%{version}.gem
# Source0-md5:	f62501746a7f13399c4d9dab917d0ee4
Patch0:		ruby-deprecated.patch
Patch1:		rpm5.patch
URL:		http://gitorious.org/ruby-rpm
BuildRequires:	rpm-devel
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-devel >= 1.8.6
%if %{with tests}
BuildRequires:	ruby-rake-compiler >= 0.7
BuildRequires:	ruby-rdiscount >= 1.6
BuildRequires:	ruby-rdoc >= 3.9
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides bindings for accessing RPM packages and databases from Ruby.
It includes the low-level C API to talk to rpm as well as Ruby classes
to model the various objects that RPM deals with (such as packages,
dependencies, and files).

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1
%patch1 -p1

%build
cd ext/%{pkgname}
ruby extconf.rb
%{__make} V=1 \
	CC="%{__cc}" \
	cppflags=-I/usr/include/rpm \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_vendorarchdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
install -p ext/%{pkgname}/%{pkgname}.so $RPM_BUILD_ROOT%{ruby_vendorarchdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc CHANGELOG.rdoc
%{ruby_vendorlibdir}/rpm.rb
%{ruby_vendorlibdir}/rpm
%attr(755,root,root) %{ruby_vendorarchdir}/rpm.so
