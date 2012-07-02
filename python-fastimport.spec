# TODO
# - fix tests to run in %build
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		module_name	fastimport
Summary:	Python parser for fastimport (VCS interchange format)
Name:		python-%{module_name}
Version:	0.9.1
Release:	1
License:	GPL v2+
Group:		Development/Languages
URL:		https://launchpad.net/python-fastimport
Source0:	http://launchpad.net/python-fastimport/trunk/%{version}/+download/%{module_name}-%{version}.tar.gz
# Source0-md5:	0c53dcce7ac4df8f1d4df436081b01bd
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	python-distribute
BuildRequires:	python-nose
BuildRequires:	python-testtools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Python parser that was originally developed for
bzr-fastimport, but extracted so it can be used by other projects.

%prep
%setup -q -n %{module_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	-O2 \
	--skip-build \
	--root $RPM_BUILD_ROOT

%if %{with tests}
PYTHONPATH=$RPM_BUILD_ROOT%{py_sitescriptdir} nosetests-%{py_ver} %{module_name}
%endif

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module_name}/tests

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%dir %{py_sitescriptdir}/%{module_name}
%{py_sitescriptdir}/%{module_name}/*.py[co]
%dir %{py_sitescriptdir}/%{module_name}/processors
%{py_sitescriptdir}/%{module_name}/processors/*.py[co]
%{py_sitescriptdir}/%{module_name}-*.egg-info
