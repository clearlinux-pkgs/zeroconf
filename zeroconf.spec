#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zeroconf
Version  : 0.32.1
Release  : 49
URL      : https://files.pythonhosted.org/packages/3a/2d/8e8d2d882031f835746bd427b4297fb475dac4a9f0afc34f4fba8bc6458d/zeroconf-0.32.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/3a/2d/8e8d2d882031f835746bd427b4297fb475dac4a9f0afc34f4fba8bc6458d/zeroconf-0.32.1.tar.gz
Summary  : Pure Python Multicast DNS Service Discovery Library (Bonjour/Avahi compatible)
Group    : Development/Tools
License  : LGPL-2.1
Requires: zeroconf-license = %{version}-%{release}
Requires: zeroconf-python = %{version}-%{release}
Requires: zeroconf-python3 = %{version}-%{release}
Requires: ifaddr
BuildRequires : buildreq-distutils3
BuildRequires : ifaddr

%description
===============

%package license
Summary: license components for the zeroconf package.
Group: Default

%description license
license components for the zeroconf package.


%package python
Summary: python components for the zeroconf package.
Group: Default
Requires: zeroconf-python3 = %{version}-%{release}

%description python
python components for the zeroconf package.


%package python3
Summary: python3 components for the zeroconf package.
Group: Default
Requires: python3-core
Provides: pypi(zeroconf)
Requires: pypi(ifaddr)

%description python3
python3 components for the zeroconf package.


%prep
%setup -q -n zeroconf-0.32.1
cd %{_builddir}/zeroconf-0.32.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1625591691
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zeroconf
cp %{_builddir}/zeroconf-0.32.1/COPYING %{buildroot}/usr/share/package-licenses/zeroconf/720ac006232639ed551ce48d638dee35f8d378d4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zeroconf/720ac006232639ed551ce48d638dee35f8d378d4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
