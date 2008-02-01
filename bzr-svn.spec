Summary:	Plugin for Bazaar-NG providing Subversion repository access
Summary(pl.UTF-8):	Wtyczka do Bazaar-NG umożliwiająca dostęp do repozytorium Subversion
Name:		bzr-svn
Version:	0.4.7
Release:	1
License:	GPL v2+
Group:		Development/Version Control
Source0:	http://samba.org/~jelmer/bzr/%{name}-%{version}.tar.gz
# Source0-md5:	fa3824ff6483647f031256f6f35eec97
URL:		http://bazaar-vcs.org/BzrForeignBranches/Subversion
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	bzr >= 0.13
Requires:	python-subversion >= 1.4.4-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bzr-svn is a plugin for Bazaar-NG providing Subversion repository
access.

%description -l pl.UTF-8
bzr-sbn jest wtyczką do Bazaar-NG umożliwiająca dostęp do repozytorium
Subversion.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--install-lib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%dir %{py_sitedir}/bzrlib/plugins/svn
%{py_sitedir}/bzrlib/plugins/svn/*.py[co]
%dir %{py_sitedir}/bzrlib/plugins/svn/tests
%{py_sitedir}/bzrlib/plugins/svn/tests/*.py[co]
%{py_sitedir}/bzr_svn-*.egg-info
