# hello-kmod
Simple spec files and supporting material to create tiny redhat kmod-(use `kernel_module_pacakge` rpm macro) and non-kmod packages for testing and reference

### Build kmod rpm
```
rpmdev-setuptree
git clone https://github.com/xin3liang/hello-kmod.git
cd hello-kmod
make dist
cp -r hello.tar kmod-hello.files kmod-hello.preamble  ~/rpmbuild/SOURCES
rpmbuild -ba hello-kmod.spec
```
