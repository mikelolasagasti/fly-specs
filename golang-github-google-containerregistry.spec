# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/google/go-containerregistry
%global goipath         github.com/google/go-containerregistry
Version:                0.9.0

%gometa

%global common_description %{expand:
Go library and CLIs for working with container registries.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md SECURITY.md README.md\\\
                        cmd/crane/README.md cmd/gcrane/README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go library and CLIs for working with container registries

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
rm -rf cmd/krane cmd/ko cmd/registry

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/crane cmd/gcrane; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md SECURITY.md README.md cmd/crane/README.md
%doc cmd/gcrane/README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
