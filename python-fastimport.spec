#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	fastimport
Summary:	Python parser for fastimport (VCS interchange format)
Summary(pl.UTF-8):	Pythonowy parser formatu fastimport (do wymiany VCS)
Name:		python-%{module}
# keep 0.9.8 here for python2 support
Version:	0.9.8
Release:	1
License:	GPL v2+
Group:		Libraries/Python
#Source0Download: https://pypi.org/project/simple/
Source0:	https://files.pythonhosted.org/packages/source/f/fastimport/%{module}-%{version}.tar.gz
# Source0-md5:	85a206e92e209937a8dd11ffe8139cf9
URL:		https://pypi.org/project/fastimport/
BuildRequires:	python-modules >= 1:2.7
%if %{with tests}
BuildRequires:	python-nose
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Python parser that was originally developed for
bzr-fastimport, but extracted so it can be used by other projects.

%description -l pl.UTF-8
Pythonowy parser, oryginalnie stworzony na potrzeby bzr-fastimport,
ale wyciągnięty do osobnego modułu, dzięki czemu może być używany
przez inne projekty.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%if %{with tests}
nosetests-%{py_ver} fastimport
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests
%py_postclean

for f in $RPM_BUILD_ROOT%{_bindir}/fast-import-* ; do
	%{__mv} "$f" "${f}-2"
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/fast-import-filter-2
%attr(755,root,root) %{_bindir}/fast-import-info-2
%attr(755,root,root) %{_bindir}/fast-import-query-2
%{py_sitescriptdir}/fastimport
%{py_sitescriptdir}/fastimport-%{version}-py*.egg-info
