#
# spec file for package yast2-dhcp-server
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           yast2-dhcp-server
Version:        4.1.5
Release:        0
Summary:        YaST2 - DHCP Server Configuration
Group:          System/YaST
License:        GPL-2.0-only
Url:            https://github.com/yast-dhcp-server

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  perl-Digest-SHA1
BuildRequires:  perl-X500-DN
BuildRequires:  perl-XML-Writer
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  libxslt
BuildRequires:  perl-XML-Writer
BuildRequires:  popt-devel
BuildRequires:  sgml-skel
BuildRequires:  update-desktop-files
BuildRequires:  yast2-perl-bindings
BuildRequires:  yast2-testsuite
BuildRequires:  yast2-dns-server
BuildRequires:  yast2-devtools >= 3.1.10
# Yast2::ServiceWidget
BuildRequires:  yast2 >= 4.1.0
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

Requires:       perl-gettext
Requires:       yast2-perl-bindings
Requires:       bind-utils
Requires:       perl-X500-DN
Requires:       yast2-ldap
Requires:       perl-Digest-SHA1
Requires:       perl-Parse-RecDescent
# firewalld_wrapper.rb
Requires:       yast2 >= 4.1.22
# DnsServerAPI::IsServiceConfigurableExternally
Requires:       yast2-dns-server >= 2.13.16
Requires:       yast2-ruby-bindings >= 1.0.0

BuildArch:      noarch

%description
This package contains the YaST2 component for DHCP server
configuration.

%prep
%setup -q

%check
%yast_check

%build
%yast_build

%install
%yast_install
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}
%{yast_agentdir}
%doc %{yast_docdir}
%license COPYING
%{yast_icondir}
%{yast_schemadir}

%changelog
