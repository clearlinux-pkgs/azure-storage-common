#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-storage-common
Version  : 1.4.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/6b/d5/b0bac239f0b6396ce6f56a04ed5e3a8e4a0fe59669459f4cf4fe9df4f259/azure-storage-common-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/6b/d5/b0bac239f0b6396ce6f56a04ed5e3a8e4a0fe59669459f4cf4fe9df4f259/azure-storage-common-1.4.0.tar.gz
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
======================================

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
%setup -q -n azure-storage-common-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545578465
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
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
