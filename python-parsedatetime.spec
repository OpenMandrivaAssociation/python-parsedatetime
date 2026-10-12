Name:		python-parsedatetime
Version:	2.6
Release:	5
Source0:	https://files.pythonhosted.org/packages/source/p/parsedatetime/parsedatetime-%{version}.tar.gz
Summary:	Parse human-readable date/time text.
URL:		https://pypi.org/project/parsedatetime/
License:	Apache License 2.0
Group:		Development/Python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
Parse human-readable date/time text.

%prep
%autosetup -p1 -n parsedatetime-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/parsedatetime
%{py_sitedir}/parsedatetime-*.*-info
