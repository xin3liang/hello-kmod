Name:           hello-kmod
Version:        1
Release:        1%{?dist}
Summary:        Kernel module(s)
License:        CDDL
Group:          System Environment/Kernel
BuildRequires:  %kernel_module_package_buildreqs
Source0:        hello.tar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Additional dependency information for the kmod sub-package must be specified
# by generating a preamble text file which kmodtool can append to the spec file.
%(/bin/echo -e "\
Requires:       hello = %{version}\n\
Conflicts:      hello-dkms\n\
Obsoletes:      spl-kmod\n\n" > %{_sourcedir}/kmod-preamble)

%description
This package contains the hello kernel module, which does nothing.

%define kmod_name hello

%kernel_module_package -n %{kmod_name} -p %{_sourcedir}/kmod-preamble

%prep
%setup -n %{kmod_name}

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/lib/modules/%{kverrel}/extra/hello/hello/
install -m 755 %{kmod_name}.ko %{buildroot}/lib/modules/%{kverrel}/extra/hello/hello/hello.ko
find %{buildroot} -type f
%{__rm} -f %{buildroot}/lib/modules/%{kverrel}/modules.*


%clean
rm -rf $RPM_BUILD_ROOT

#%files
# not sure why this isn't necessary

%changelog
# let's skip this for now
