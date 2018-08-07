#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-perf
Version  : 1.5.1
Release  : 1
URL      : https://files.pythonhosted.org/packages/79/75/3c5d3565c81e662e7ab4d2a838a0808c1508718a93557e452111bb2a0815/perf-1.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/79/75/3c5d3565c81e662e7ab4d2a838a0808c1508718a93557e452111bb2a0815/perf-1.5.1.tar.gz
Summary  : Python module to generate and modify perf
Group    : Development/Tools
License  : MIT
Requires: python-perf-bin
Requires: python-perf-python3
Requires: python-perf-python
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
perf
        ****

%package bin
Summary: bin components for the python-perf package.
Group: Binaries

%description bin
bin components for the python-perf package.


%package python
Summary: python components for the python-perf package.
Group: Default
Requires: python-perf-python3

%description python
python components for the python-perf package.


%package python3
Summary: python3 components for the python-perf package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-perf package.


%prep
%setup -q -n perf-1.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533681625
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyperf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
