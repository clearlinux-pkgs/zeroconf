#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zeroconf
Version  : 0.37.0
Release  : 71
URL      : https://files.pythonhosted.org/packages/5e/82/791c22d47f4622ce83553756461b682a0a1be1cbc0251201c6cf58a3fd66/zeroconf-0.37.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5e/82/791c22d47f4622ce83553756461b682a0a1be1cbc0251201c6cf58a3fd66/zeroconf-0.37.0.tar.gz
Summary  : Pure Python Multicast DNS Service Discovery Library (Bonjour/Avahi compatible)
Group    : Development/Tools
License  : LGPL-2.1
Requires: zeroconf-license = %{version}-%{release}
Requires: zeroconf-python = %{version}-%{release}
Requires: zeroconf-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(ifaddr)

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
%setup -q -n zeroconf-0.37.0
cd %{_builddir}/zeroconf-0.37.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637282864
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zeroconf
cp %{_builddir}/zeroconf-0.37.0/COPYING %{buildroot}/usr/share/package-licenses/zeroconf/ab7752f30a9ae392de622ae6220b1034bbb4767a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zeroconf/ab7752f30a9ae392de622ae6220b1034bbb4767a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
