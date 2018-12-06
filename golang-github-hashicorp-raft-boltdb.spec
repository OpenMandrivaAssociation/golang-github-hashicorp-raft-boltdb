# http://github.com/hashicorp/raft-boltdb

%global goipath         github.com/hashicorp/raft-boltdb
%global commit          d1e82c1ec3f15ee991f7cc7ffd5b67ff6f5bbaee


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.13%{?dist}
Summary:        Raft backend implementation using BoltDB
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/boltdb/bolt)
BuildRequires: golang(github.com/hashicorp/go-msgpack/codec)
BuildRequires: golang(github.com/hashicorp/raft)
BuildRequires: golang(github.com/hashicorp/raft/bench)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.gitd1e82c1
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.20150101gitd1e82c1
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitd1e82c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitd1e82c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitd1e82c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitd1e82c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.gitd1e82c1
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.gitd1e82c1
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitd1e82c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gitd1e82c1
- Update to spec-2.1
  related: #1250474

* Thu Aug 06 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.gitd1e82c1
- Update spec file to spec-2.0
  resolves: #1250474

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitd1e82c1
- First package for Fedora
  resolves: #1212105

