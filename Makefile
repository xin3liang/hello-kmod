# If KERNELRELEASE is defined, we've been invoked from the
# kernel build system and can use its language.
ifneq ($(KERNELRELEASE),)
 obj-m := hello.o
# Otherwise we were called directly from the command
# line; invoke the kernel build system.
else
 KERNELDIR ?= /lib/modules/$(shell uname -r)/build
 PWD := $(shell pwd)

default:
	$(MAKE) -C $(KERNELDIR) M=$(PWD) modules

clean:
	rm -f hello.{ko,mod.c,mod.o,o,mod}
	rm -f modules.order Module.symvers 
	rm -f  .*.cmd
	rm -rf hello/ hello.tar

dist:
	mkdir -p hello
	cp hello.c Makefile hello
	tar cf hello.tar hello

test: hello.ko
	lsmod | grep hello || echo OK module not loaded
	sudo insmod ./hello.ko
	sudo rmmod hello
	lsmod | grep hello || echo OK module not loaded
	sudo dmesg | tail -n 2

endif

# The module name is determined by the obj-m assignment above.
# This name is both the basename of the .ko file as well as
# the name that appears in lsmod, /sys/modules/, and probably
# everywhere.
