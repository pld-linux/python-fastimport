# TODO
# - fix tests to run in %build
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		module	fastimport
Summary:	Python parser for fastimport (VCS interchange format)
Name:		python-%{module}
Version:	0.9.2
Release:	1
License:	GPL v2+
Group:		Development/Languages
Source0:	http://launchpad.net/python-fastimport/trunk/%{version}/+download/%{module}-%{version}.tar.gz
# Source0-md5:	68972ad820785ec3247ec7bad0bfa6ea
URL:		https://launchpad.net/python-fastimport
BuildRequires:	python-distribute
BuildRequires:	python-nose
BuildRequires:	python-testtools
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Python parser that was originally developed for
bzr-fastimport, but extracted so it can be used by other projects.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	-O2 \
	--skip-build \
	--root $RPM_BUILD_ROOT

%if %{with tests}
PYTHONPATH=$RPM_BUILD_ROOT%{py_sitescriptdir} nosetests-%{py_ver} %{module}
%endif

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/processors
%{py_sitescriptdir}/%{module}/processors/*.py[co]
%{py_sitescriptdir}/%{module}-*.egg-info
