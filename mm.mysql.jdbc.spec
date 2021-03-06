#
# Conditional build:
%bcond_with	binary		# use binary jar instead of compiling

%define java_version %(IFS=.; set -- $(%java -fullversion 2>&1 | grep -o '".*"' | xargs); echo "$1.$2")
%if "%{java_version}" >= "1.4"
%define	with_binary 1
%endif
Summary:	MM.MySQL is A Type IV JDBC driver for MySQL
Name:		mm.mysql.jdbc
Version:	1.2c
Release:	1
License:	LGPL v2
Group:		Development/Languages/Java
URL:		http://mmmysql.sourceforge.net/oldDist.html
Source0:	http://mmmysql.sourceforge.net/dist/%{name}-%{version}.tar.gz
# Source0-md5:	b04aa7f3048c2ebb169ee88ce19a6a4c
%{!?with_binary:BuildRequires:	jdk < 1.4}
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Obsoletes:	java-mysql-connector
Obsoletes:	java-mysql-mm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MM.MySQL is A Type IV JDBC driver for MySQL.

NOTE: This is old unsupported driver, you should really use MySQL
Connector/J from <http://dev.mysql.com/downloads/connector/j/>.

%prep
%setup -q
mv mysql_comp.jar %{name}.jar

%if %{without binary}
%build
%javac -source 1.2 -target 1.2 org/gjt/mm/mysql/*.java
%jar -cvf %{name}.jar org/gjt/mm/mysql/*.class
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
# jars
cp -a %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{_javadir}/*.jar
