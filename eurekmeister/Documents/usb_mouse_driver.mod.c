#include <linux/module.h>
#include <linux/export-internal.h>
#include <linux/compiler.h>

MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};



static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0x44966a4e, "usb_register_driver" },
	{ 0x441dcc96, "input_unregister_device" },
	{ 0x37a0cba, "kfree" },
	{ 0x6990c8f2, "usb_deregister" },
	{ 0x6568f461, "kmalloc_caches" },
	{ 0xb104dc7c, "__kmalloc_cache_noprof" },
	{ 0xe1bf6e, "input_allocate_device" },
	{ 0xf66ea036, "input_register_device" },
	{ 0xc2c3a3b1, "input_free_device" },
	{ 0x47e64c59, "module_layout" },
};

MODULE_INFO(depends, "");

MODULE_ALIAS("usb:v10C4p8105d*dc*dsc*dp*ic*isc*ip*in*");

MODULE_INFO(srcversion, "3F2A3E27A58A77F6AA4ECA7");
