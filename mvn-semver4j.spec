#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-semver4j
Version  : 2.2.0
Release  : 2
URL      : https://github.com/vdurmont/semver4j/archive/v2.2.0.tar.gz
Source0  : https://github.com/vdurmont/semver4j/archive/v2.2.0.tar.gz
Source1  : https://repo1.maven.org/maven2/com/vdurmont/semver4j/2.1.0/semver4j-2.1.0.jar
Source2  : https://repo1.maven.org/maven2/com/vdurmont/semver4j/2.1.0/semver4j-2.1.0.pom
Source3  : https://repo1.maven.org/maven2/com/vdurmont/semver4j/2.2.0/semver4j-2.2.0.jar
Source4  : https://repo1.maven.org/maven2/com/vdurmont/semver4j/2.2.0/semver4j-2.2.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-semver4j-data = %{version}-%{release}
Requires: mvn-semver4j-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
# Semver4j
> This library is under development and no stable version has been released yet.
> The API can change at any moment.

%package data
Summary: data components for the mvn-semver4j package.
Group: Data

%description data
data components for the mvn-semver4j package.


%package license
Summary: license components for the mvn-semver4j package.
Group: Default

%description license
license components for the mvn-semver4j package.


%prep
%setup -q -n semver4j-2.2.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-semver4j
cp LICENSE.md %{buildroot}/usr/share/package-licenses/mvn-semver4j/LICENSE.md
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/vdurmont/semver4j/2.1.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/vdurmont/semver4j/2.1.0/semver4j-2.1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/vdurmont/semver4j/2.1.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/vdurmont/semver4j/2.1.0/semver4j-2.1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/vdurmont/semver4j/2.2.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/vdurmont/semver4j/2.2.0/semver4j-2.2.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/vdurmont/semver4j/2.2.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/vdurmont/semver4j/2.2.0/semver4j-2.2.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/vdurmont/semver4j/2.1.0/semver4j-2.1.0.jar
/usr/share/java/.m2/repository/com/vdurmont/semver4j/2.1.0/semver4j-2.1.0.pom
/usr/share/java/.m2/repository/com/vdurmont/semver4j/2.2.0/semver4j-2.2.0.jar
/usr/share/java/.m2/repository/com/vdurmont/semver4j/2.2.0/semver4j-2.2.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-semver4j/LICENSE.md
