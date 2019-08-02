#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-storage-common
Version  : 2.1.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/48/12/e074fe454bc327fbe2a61e20d3260473ee4a0fd85387baf249dc83c8e774/azure-storage-common-2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/48/12/e074fe454bc327fbe2a61e20d3260473ee4a0fd85387baf249dc83c8e774/azure-storage-common-2.1.0.tar.gz
Summary  : Microsoft Azure Storage Common Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-storage-common-license = %{version}-%{release}
Requires: azure-storage-common-python = %{version}-%{release}
Requires: azure-storage-common-python3 = %{version}-%{release}
Requires: azure-common
Requires: cryptography
Requires: python-dateutil
Requires: requests
BuildRequires : azure-common
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : python-dateutil
BuildRequires : requests

%description
Microsoft Azure Storage SDK for Python
======================================
.. image:: https://travis-ci.org/Azure/azure-storage-python.svg
:target: https://travis-ci.org/Azure/azure-storage-python
.. image:: https://img.shields.io/codecov/c/github/azure/azure-storage-python.svg
:target: https://codecov.io/gh/Azure/azure-storage-python

%package license
Summary: license components for the azure-storage-common package.
Group: Default

%description license
license components for the azure-storage-common package.


%package python
Summary: python components for the azure-storage-common package.
Group: Default
Requires: azure-storage-common-python3 = %{version}-%{release}

%description python
python components for the azure-storage-common package.


%package python3
Summary: python3 components for the azure-storage-common package.
Group: Default
Requires: python3-core

%description python3
python3 components for the azure-storage-common package.


%prep
%setup -q -n azure-storage-common-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1564754015
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/azure-storage-common
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/azure-storage-common/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/azure-storage-common/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
