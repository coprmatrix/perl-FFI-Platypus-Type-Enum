#
# spec file for package perl-FFI-Platypus-Type-Enum (Version 0.06)
#
# Copyright (c) 124 SUSE LLC
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

%define cpan_name FFI-Platypus-Type-Enum
Name:           perl-FFI-Platypus-Type-Enum
Version:        0.06
Release:        0
License:   Artistic-1.0 or GPL-1.0-or-later
Summary:        Custom platypus type for dealing with C enumerated types
Url:            https://metacpan.org/release/%{cpan_name}
Source0:         https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-macros-suse
BuildRequires:  perl-generators
BuildRequires:  perl(constant) >= 1.32
BuildRequires:  perl(FFI::Platypus) >= 1.00
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Test2::V0) >= 0.000121
Requires:       perl(constant) >= 1.32
Requires:       perl(Ref::Util)

%description
This type plugin is a helper for making enumerated types. It makes the most
sense to use this when you have an enumerated type with a small number of
possible values. For a large set of enumerated values or constants, see
FFI::Platypus::Constant.

This type plugin has two modes:

* string

In string mode, string representations of the enum values are converted
into the integer enum values when passed into C, and the enums are
converted back into strings when coming from C back into Perl. You can also
pass in the integer values.

* constant

In constant mode, constants are defined in the specified package, and with
the optional prefix. The string representation or integer constants can be
passed into C, but the integer constants are returned from C back into
Perl.

In both modes, if you attempt to pass in a value that isn't one of the
possible enum values, an exception will be thrown.

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
