#include <linux/init.h>
#include <linux/module.h>
#include <linux/fs.h>
#include <linux/cdev.h>
#include <linux/slab.h>
#include <asm/uaccess.h>

MODULE_LICENSE("GPL");

static int the_olaf_module_init(void)
{
 	printk(KERN_ALERT "Hello, world %d\n", 99);

	return 0;
}
module_init(the_olaf_module_init);

static void the_olaf_module_exit(void)
{
	printk(KERN_ALERT "Goodbye, cruel world %d\n", 0);
}
module_exit(the_olaf_module_exit);
