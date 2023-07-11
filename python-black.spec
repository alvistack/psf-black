# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-black
Epoch: 100
Version: 23.3.0
Release: 1%{?dist}
BuildArch: noarch
Summary: The uncompromising code formatter
License: MIT
URL: https://github.com/psf/black/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Black is the uncompromising Python code formatter. By using it, you
agree to cede control over minutiae of hand-formatting. In return, Black
gives you speed, determinism, and freedom from pycodestyle nagging about
formatting. You will save time and mental energy for more important
matters.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%package -n black
Summary: The uncompromising code formatter
Requires: python3
Requires: python3-click >= 8.0.0
Requires: python3-mypy-extensions >= 0.4.3
Requires: python3-packaging >= 22.0
Requires: python3-pathspec >= 0.9.0
Requires: python3-platformdirs >= 2
Requires: python3-tomli >= 1.1.0
Requires: python3-typed-ast >= 1.4.2
Requires: python3-typing-extensions >= 3.10.0.0
Provides: python3-black = %{epoch}:%{version}-%{release}
Provides: python3dist(black) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-black = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(black) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-black = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(black) = %{epoch}:%{version}-%{release}

%description -n black
Black is the uncompromising Python code formatter. By using it, you
agree to cede control over minutiae of hand-formatting. In return, Black
gives you speed, determinism, and freedom from pycodestyle nagging about
formatting. You will save time and mental energy for more important
matters.

%files -n black
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*

%changelog
