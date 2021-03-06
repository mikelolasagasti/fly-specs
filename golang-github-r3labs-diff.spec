# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/r3labs/diff
%global goipath         github.com/r3labs/diff
Version:                3.0.0

%gometa

%global common_description %{expand:
A library for diffing golang structures.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A library for diffing golang structures

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/stretchr/testify)

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
