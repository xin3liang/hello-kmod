Name:           hello-kmod
Version:        1
Release:        1%{?dist}
Summary:        Kernel module(s)
License:        CDDL
Group:          System Environment/Kernel
BuildRequires:  %kernel_module_package_buildreqs
Source0:        hello.tar
Source1:        kmod-hello.preamble
Source2:        kmod-hello.files
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package contains the hello kernel module, which does nothing.

%define kmod_name hello
%global modules_path /lib/modules/%{kverrel}/extra/hello

%kernel_module_package -n %{kmod_name} -p %{SOURCE1} -f %{SOURCE2}

%prep
%setup -n %{kmod_name}

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{modules_path}
%{__install} -m 755 hello.ko %{buildroot}/%{modules_path}/hello.ko

%clean
rm -rf $RPM_BUILD_ROOT

#%files
# not sure why this isn't necessary

%changelog
# let's skip this for now
