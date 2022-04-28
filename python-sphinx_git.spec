#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	git Changelog for Sphinx
Summary(pl.UTF-8):	Gitowy log zmian dla Sphinksa
Name:		python-sphinx_git
Version:	11.0.0
Release:	1
License:	GPL v3+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-git/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-git/sphinx-git-%{version}.tar.gz
# Source0-md5:	5d412c4acfb6f17dfa10898c7242e6bf
URL:		https://pypi.org/project/sphinx-git/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinx-git is an extension to the Sphinx documentation tool that
allows you to include excerpts from your git history within your
documentation. This could be used for release changelogs, to pick out
specific examples of history in documentation, or just to surface what
is happening in the project.

%description -l pl.UTF-8
sphinx-git to rozszerzenie narzędzia do dokumentacji Sphinx,
pozwalające na włączanie fragmentów z historii gita do dokumentacji.
Można tego użyć do logów zmian wydań, wyciągania do dokumentacji
określonych przykładów historii lub pokazania, co się dzieje w
projekcie.

%package -n python3-sphinx_git
Summary:	git Changelog for Sphinx
Summary(pl.UTF-8):	Gitowy log zmian dla Sphinksa
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-sphinx_git
sphinx-git is an extension to the Sphinx documentation tool that
allows you to include excerpts from your git history within your
documentation. This could be used for release changelogs, to pick out
specific examples of history in documentation, or just to surface what
is happening in the project.

%description -n python3-sphinx_git -l pl.UTF-8
sphinx-git to rozszerzenie narzędzia do dokumentacji Sphinx,
pozwalające na włączanie fragmentów z historii gita do dokumentacji.
Można tego użyć do logów zmian wydań, wyciągania do dokumentacji
określonych przykładów historii lub pokazania, co się dzieje w
projekcie.

%prep
%setup -q -n sphinx-git-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG README.rst
%{py_sitescriptdir}/sphinx_git
%{py_sitescriptdir}/sphinx_git-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx_git
%defattr(644,root,root,755)
%doc CHANGELOG README.rst
%{py3_sitescriptdir}/sphinx_git
%{py3_sitescriptdir}/sphinx_git-%{version}-py*.egg-info
%endif
