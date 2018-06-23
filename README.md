# gdb_export
A simple tool to generate gdb debug output for some program and its core dump.

## Usage
python3 gdb_export [-b, --binary, -c, --core] [-i, --info]

## Result
A gdb.txt file that looks roughly like this 

#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff7a2df5d in __GI_abort () at abort.c:90
#2  0x00007ffff7a7628d in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff7b9d528 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:181
#3  0x00007ffff7a7d64a in malloc_printerr (action=<optimized out>, str=0x7ffff7b99fc2 "realloc(): invalid pointer", ptr=<optimized out>, ar_ptr=<optimized out>) at malloc.c:5426
#4  0x00007ffff7a84c29 in __GI___libc_realloc (oldmem=0x555555554bac, bytes=2) at malloc.c:3196
#5  0x00005555555548f1 in ?? ()
#6  0x00007ffff7dd1fc0 in re_comp_buf () from /lib/x86_64-linux-gnu/libc.so.6
#7  0x000002bc00000000 in ?? ()
#8  0x0000000000000000 in ?? ()
rax            0x0	0
rbx            0x7fffffffdcd0	140737488346320
rcx            0x7ffff7a2c0bb	140737348026555
rdx            0x0	0
rsi            0x7fffffffda10	140737488345616
rdi            0x2	2
rbp            0x7fffffffdec0	0x7fffffffdec0
rsp            0x7fffffffda10	0x7fffffffda10
r8             0x0	0
r9             0x7fffffffda10	140737488345616
r10            0x8	8
r11            0x246	582
r12            0x7fffffffdcd0	140737488346320
r13            0x7ffff7ff6000	140737354096640
r14            0x0	0
r15            0x30	48
rip            0x7ffff7a2c0bb	0x7ffff7a2c0bb <__GI_raise+203>
eflags         0x246	[ PF ZF IF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0
Stack level 0, frame at 0x7fffffffdb30:
 rip = 0x7ffff7a2c0bb in __GI_raise (../sysdeps/unix/sysv/linux/raise.c:51); saved rip = 0x7ffff7a2df5d
 called by frame at 0x7fffffffdc60
 source language c.
 Arglist at 0x7fffffffda08, args: sig=sig@entry=6
 Locals at 0x7fffffffda08, Previous frame's sp is 0x7fffffffdb30
 Saved registers:
  rip at 0x7fffffffdb28
0x7fffffffda10:	0x00000000	0x00000000	0xf7dd0720	0x00007fff
0x7fffffffda20:	0xf7ffd9d0	0x00007fff	0xf7dd5398	0x00007fff
0x7fffffffda30:	0xf7dd5650	0x00007fff	0x00000008	0x00000030
0x7fffffffda40:	0xffffdf70	0x00007fff	0xffffdeb0	0x00007fff
0x7fffffffda50:	0xf7a68ac0	0x00007fff	0xf7dd0720	0x00007fff
0x7fffffffda60:	0xffffdaf4	0x00007fff	0xf7ddf361	0x00007fff
0x7fffffffda70:	0xf7fd4510	0x00007fff	0x00000008	0x00000030
0x7fffffffda80:	0xffffdfb0	0x00007fff	0xffffdef0	0x00007fff
0x7fffffffda90:	0x7fffffff	0xfffffffe	0xffffffff	0xffffffff
0x7fffffffdaa0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdab0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdac0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdad0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdae0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdaf0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdb00:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdb10:	0xf7ff6000	0x00007fff	0x9bf00700	0xa5566466
0x7fffffffdb20:	0x00000030	0x00000000	0xf7a2df5d	0x00007fff
0x7fffffffdb30:	0x00000020	0x00000000	0x00000000	0x00000000
0x7fffffffdb40:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb50:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb60:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb70:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb80:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb90:	0x00000000	0x00000000	0x00000000	0x00000000
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff7a2df5d in __GI_abort () at abort.c:90
#2  0x00007ffff7a7628d in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff7b9d528 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:181
#3  0x00007ffff7a7d64a in malloc_printerr (action=<optimized out>, str=0x7ffff7b99fc2 "realloc(): invalid pointer", ptr=<optimized out>, ar_ptr=<optimized out>) at malloc.c:5426
#4  0x00007ffff7a84c29 in __GI___libc_realloc (oldmem=0x555555554bac, bytes=2) at malloc.c:3196
#5  0x00005555555548f1 in ?? ()
#6  0x00007ffff7dd1fc0 in re_comp_buf () from /lib/x86_64-linux-gnu/libc.so.6
#7  0x000002bc00000000 in ?? ()
#8  0x0000000000000000 in ?? ()
./blah.gds:6: Error in sourced command file:
The program is not being run.
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff7a2df5d in __GI_abort () at abort.c:90
#2  0x00007ffff7a7628d in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff7b9d528 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:181
#3  0x00007ffff7a7d64a in malloc_printerr (action=<optimized out>, str=0x7ffff7b99fc2 "realloc(): invalid pointer", ptr=<optimized out>, ar_ptr=<optimized out>) at malloc.c:5426
#4  0x00007ffff7a84c29 in __GI___libc_realloc (oldmem=0x555555554bac, bytes=2) at malloc.c:3196
#5  0x00005555555548f1 in ?? ()
#6  0x00007ffff7dd1fc0 in re_comp_buf () from /lib/x86_64-linux-gnu/libc.so.6
#7  0x000002bc00000000 in ?? ()
#8  0x0000000000000000 in ?? ()
rax            0x0	0
rbx            0x7fffffffdcd0	140737488346320
rcx            0x7ffff7a2c0bb	140737348026555
rdx            0x0	0
rsi            0x7fffffffda10	140737488345616
rdi            0x2	2
rbp            0x7fffffffdec0	0x7fffffffdec0
rsp            0x7fffffffda10	0x7fffffffda10
r8             0x0	0
r9             0x7fffffffda10	140737488345616
r10            0x8	8
r11            0x246	582
r12            0x7fffffffdcd0	140737488346320
r13            0x7ffff7ff6000	140737354096640
r14            0x0	0
r15            0x30	48
rip            0x7ffff7a2c0bb	0x7ffff7a2c0bb <__GI_raise+203>
eflags         0x246	[ PF ZF IF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0
Stack level 0, frame at 0x7fffffffdb30:
 rip = 0x7ffff7a2c0bb in __GI_raise (../sysdeps/unix/sysv/linux/raise.c:51); saved rip = 0x7ffff7a2df5d
 called by frame at 0x7fffffffdc60
 source language c.
 Arglist at 0x7fffffffda08, args: sig=sig@entry=6
 Locals at 0x7fffffffda08, Previous frame's sp is 0x7fffffffdb30
 Saved registers:
  rip at 0x7fffffffdb28
0x7fffffffda10:	0x00000000	0x00000000	0xf7dd0720	0x00007fff
0x7fffffffda20:	0xf7ffd9d0	0x00007fff	0xf7dd5398	0x00007fff
0x7fffffffda30:	0xf7dd5650	0x00007fff	0x00000008	0x00000030
0x7fffffffda40:	0xffffdf70	0x00007fff	0xffffdeb0	0x00007fff
0x7fffffffda50:	0xf7a68ac0	0x00007fff	0xf7dd0720	0x00007fff
0x7fffffffda60:	0xffffdaf4	0x00007fff	0xf7ddf361	0x00007fff
0x7fffffffda70:	0xf7fd4510	0x00007fff	0x00000008	0x00000030
0x7fffffffda80:	0xffffdfb0	0x00007fff	0xffffdef0	0x00007fff
0x7fffffffda90:	0x7fffffff	0xfffffffe	0xffffffff	0xffffffff
0x7fffffffdaa0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdab0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdac0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdad0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdae0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdaf0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdb00:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdb10:	0xf7ff6000	0x00007fff	0x9bf00700	0xa5566466
0x7fffffffdb20:	0x00000030	0x00000000	0xf7a2df5d	0x00007fff
0x7fffffffdb30:	0x00000020	0x00000000	0x00000000	0x00000000
0x7fffffffdb40:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb50:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb60:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb70:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb80:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb90:	0x00000000	0x00000000	0x00000000	0x00000000
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff7a2df5d in __GI_abort () at abort.c:90
#2  0x00007ffff7a7628d in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff7b9d528 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:181
#3  0x00007ffff7a7d64a in malloc_printerr (action=<optimized out>, str=0x7ffff7b99fc2 "realloc(): invalid pointer", ptr=<optimized out>, ar_ptr=<optimized out>) at malloc.c:5426
#4  0x00007ffff7a84c29 in __GI___libc_realloc (oldmem=0x555555554bac, bytes=2) at malloc.c:3196
#5  0x00005555555548f1 in ?? ()
#6  0x00007ffff7dd1fc0 in re_comp_buf () from /lib/x86_64-linux-gnu/libc.so.6
#7  0x000002bc00000000 in ?? ()
#8  0x0000000000000000 in ?? ()
rax            0x0	0
rbx            0x7fffffffdcd0	140737488346320
rcx            0x7ffff7a2c0bb	140737348026555
rdx            0x0	0
rsi            0x7fffffffda10	140737488345616
rdi            0x2	2
rbp            0x7fffffffdec0	0x7fffffffdec0
rsp            0x7fffffffda10	0x7fffffffda10
r8             0x0	0
r9             0x7fffffffda10	140737488345616
r10            0x8	8
r11            0x246	582
r12            0x7fffffffdcd0	140737488346320
r13            0x7ffff7ff6000	140737354096640
r14            0x0	0
r15            0x30	48
rip            0x7ffff7a2c0bb	0x7ffff7a2c0bb <__GI_raise+203>
eflags         0x246	[ PF ZF IF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0
Stack level 0, frame at 0x7fffffffdb30:
 rip = 0x7ffff7a2c0bb in __GI_raise (../sysdeps/unix/sysv/linux/raise.c:51); saved rip = 0x7ffff7a2df5d
 called by frame at 0x7fffffffdc60
 source language c.
 Arglist at 0x7fffffffda08, args: sig=sig@entry=6
 Locals at 0x7fffffffda08, Previous frame's sp is 0x7fffffffdb30
 Saved registers:
  rip at 0x7fffffffdb28
0x7fffffffda10:	0x00000000	0x00000000	0xf7dd0720	0x00007fff
0x7fffffffda20:	0xf7ffd9d0	0x00007fff	0xf7dd5398	0x00007fff
0x7fffffffda30:	0xf7dd5650	0x00007fff	0x00000008	0x00000030
0x7fffffffda40:	0xffffdf70	0x00007fff	0xffffdeb0	0x00007fff
0x7fffffffda50:	0xf7a68ac0	0x00007fff	0xf7dd0720	0x00007fff
0x7fffffffda60:	0xffffdaf4	0x00007fff	0xf7ddf361	0x00007fff
0x7fffffffda70:	0xf7fd4510	0x00007fff	0x00000008	0x00000030
0x7fffffffda80:	0xffffdfb0	0x00007fff	0xffffdef0	0x00007fff
0x7fffffffda90:	0x7fffffff	0xfffffffe	0xffffffff	0xffffffff
0x7fffffffdaa0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdab0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdac0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdad0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdae0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdaf0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdb00:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdb10:	0xf7ff6000	0x00007fff	0x9bf00700	0xa5566466
0x7fffffffdb20:	0x00000030	0x00000000	0xf7a2df5d	0x00007fff
0x7fffffffdb30:	0x00000020	0x00000000	0x00000000	0x00000000
0x7fffffffdb40:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb50:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb60:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb70:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb80:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb90:	0x00000000	0x00000000	0x00000000	0x00000000
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff7a2df5d in __GI_abort () at abort.c:90
#2  0x00007ffff7a7628d in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff7b9d528 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:181
#3  0x00007ffff7a7d64a in malloc_printerr (action=<optimized out>, str=0x7ffff7b99fc2 "realloc(): invalid pointer", ptr=<optimized out>, ar_ptr=<optimized out>) at malloc.c:5426
#4  0x00007ffff7a84c29 in __GI___libc_realloc (oldmem=0x555555554bac, bytes=2) at malloc.c:3196
#5  0x00005555555548f1 in ?? ()
#6  0x00007ffff7dd1fc0 in re_comp_buf () from /lib/x86_64-linux-gnu/libc.so.6
#7  0x000002bc00000000 in ?? ()
#8  0x0000000000000000 in ?? ()
rax            0x0	0
rbx            0x7fffffffdcd0	140737488346320
rcx            0x7ffff7a2c0bb	140737348026555
rdx            0x0	0
rsi            0x7fffffffda10	140737488345616
rdi            0x2	2
rbp            0x7fffffffdec0	0x7fffffffdec0
rsp            0x7fffffffda10	0x7fffffffda10
r8             0x0	0
r9             0x7fffffffda10	140737488345616
r10            0x8	8
r11            0x246	582
r12            0x7fffffffdcd0	140737488346320
r13            0x7ffff7ff6000	140737354096640
r14            0x0	0
r15            0x30	48
rip            0x7ffff7a2c0bb	0x7ffff7a2c0bb <__GI_raise+203>
eflags         0x246	[ PF ZF IF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0
Stack level 0, frame at 0x7fffffffdb30:
 rip = 0x7ffff7a2c0bb in __GI_raise (../sysdeps/unix/sysv/linux/raise.c:51); saved rip = 0x7ffff7a2df5d
 called by frame at 0x7fffffffdc60
 source language c.
 Arglist at 0x7fffffffda08, args: sig=sig@entry=6
 Locals at 0x7fffffffda08, Previous frame's sp is 0x7fffffffdb30
 Saved registers:
  rip at 0x7fffffffdb28
0x7fffffffda10:	0x00000000	0x00000000	0xf7dd0720	0x00007fff
0x7fffffffda20:	0xf7ffd9d0	0x00007fff	0xf7dd5398	0x00007fff
0x7fffffffda30:	0xf7dd5650	0x00007fff	0x00000008	0x00000030
0x7fffffffda40:	0xffffdf70	0x00007fff	0xffffdeb0	0x00007fff
0x7fffffffda50:	0xf7a68ac0	0x00007fff	0xf7dd0720	0x00007fff
0x7fffffffda60:	0xffffdaf4	0x00007fff	0xf7ddf361	0x00007fff
0x7fffffffda70:	0xf7fd4510	0x00007fff	0x00000008	0x00000030
0x7fffffffda80:	0xffffdfb0	0x00007fff	0xffffdef0	0x00007fff
0x7fffffffda90:	0x7fffffff	0xfffffffe	0xffffffff	0xffffffff
0x7fffffffdaa0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdab0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdac0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdad0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdae0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdaf0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdb00:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdb10:	0xf7ff6000	0x00007fff	0x9bf00700	0xa5566466
0x7fffffffdb20:	0x00000030	0x00000000	0xf7a2df5d	0x00007fff
0x7fffffffdb30:	0x00000020	0x00000000	0x00000000	0x00000000
0x7fffffffdb40:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb50:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb60:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb70:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb80:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb90:	0x00000000	0x00000000	0x00000000	0x00000000
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff7a2df5d in __GI_abort () at abort.c:90
#2  0x00007ffff7a7628d in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff7b9d528 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:181
#3  0x00007ffff7a7d64a in malloc_printerr (action=<optimized out>, str=0x7ffff7b99fc2 "realloc(): invalid pointer", ptr=<optimized out>, ar_ptr=<optimized out>) at malloc.c:5426
#4  0x00007ffff7a84c29 in __GI___libc_realloc (oldmem=0x555555554bac, bytes=2) at malloc.c:3196
#5  0x00005555555548f1 in ?? ()
#6  0x00007ffff7dd1fc0 in re_comp_buf () from /lib/x86_64-linux-gnu/libc.so.6
#7  0x000002bc00000000 in ?? ()
#8  0x0000000000000000 in ?? ()
rax            0x0	0
rbx            0x7fffffffdcd0	140737488346320
rcx            0x7ffff7a2c0bb	140737348026555
rdx            0x0	0
rsi            0x7fffffffda10	140737488345616
rdi            0x2	2
rbp            0x7fffffffdec0	0x7fffffffdec0
rsp            0x7fffffffda10	0x7fffffffda10
r8             0x0	0
r9             0x7fffffffda10	140737488345616
r10            0x8	8
r11            0x246	582
r12            0x7fffffffdcd0	140737488346320
r13            0x7ffff7ff6000	140737354096640
r14            0x0	0
r15            0x30	48
rip            0x7ffff7a2c0bb	0x7ffff7a2c0bb <__GI_raise+203>
eflags         0x246	[ PF ZF IF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0
Stack level 0, frame at 0x7fffffffdb30:
 rip = 0x7ffff7a2c0bb in __GI_raise (../sysdeps/unix/sysv/linux/raise.c:51); saved rip = 0x7ffff7a2df5d
 called by frame at 0x7fffffffdc60
 source language c.
 Arglist at 0x7fffffffda08, args: sig=sig@entry=6
 Locals at 0x7fffffffda08, Previous frame's sp is 0x7fffffffdb30
 Saved registers:
  rip at 0x7fffffffdb28
0x7fffffffda10:	0x00000000	0x00000000	0xf7dd0720	0x00007fff
0x7fffffffda20:	0xf7ffd9d0	0x00007fff	0xf7dd5398	0x00007fff
0x7fffffffda30:	0xf7dd5650	0x00007fff	0x00000008	0x00000030
0x7fffffffda40:	0xffffdf70	0x00007fff	0xffffdeb0	0x00007fff
0x7fffffffda50:	0xf7a68ac0	0x00007fff	0xf7dd0720	0x00007fff
0x7fffffffda60:	0xffffdaf4	0x00007fff	0xf7ddf361	0x00007fff
0x7fffffffda70:	0xf7fd4510	0x00007fff	0x00000008	0x00000030
0x7fffffffda80:	0xffffdfb0	0x00007fff	0xffffdef0	0x00007fff
0x7fffffffda90:	0x7fffffff	0xfffffffe	0xffffffff	0xffffffff
0x7fffffffdaa0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdab0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdac0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdad0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdae0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdaf0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdb00:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdb10:	0xf7ff6000	0x00007fff	0x9bf00700	0xa5566466
0x7fffffffdb20:	0x00000030	0x00000000	0xf7a2df5d	0x00007fff
0x7fffffffdb30:	0x00000020	0x00000000	0x00000000	0x00000000
0x7fffffffdb40:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb50:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb60:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb70:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb80:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb90:	0x00000000	0x00000000	0x00000000	0x00000000
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff7a2df5d in __GI_abort () at abort.c:90
#2  0x00007ffff7a7628d in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff7b9d528 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:181
#3  0x00007ffff7a7d64a in malloc_printerr (action=<optimized out>, str=0x7ffff7b99fc2 "realloc(): invalid pointer", ptr=<optimized out>, ar_ptr=<optimized out>) at malloc.c:5426
#4  0x00007ffff7a84c29 in __GI___libc_realloc (oldmem=0x555555554bac, bytes=2) at malloc.c:3196
#5  0x00005555555548f1 in ?? ()
#6  0x00007ffff7dd1fc0 in re_comp_buf () from /lib/x86_64-linux-gnu/libc.so.6
#7  0x000002bc00000000 in ?? ()
#8  0x0000000000000000 in ?? ()
rax            0x0	0
rbx            0x7fffffffdcd0	140737488346320
rcx            0x7ffff7a2c0bb	140737348026555
rdx            0x0	0
rsi            0x7fffffffda10	140737488345616
rdi            0x2	2
rbp            0x7fffffffdec0	0x7fffffffdec0
rsp            0x7fffffffda10	0x7fffffffda10
r8             0x0	0
r9             0x7fffffffda10	140737488345616
r10            0x8	8
r11            0x246	582
r12            0x7fffffffdcd0	140737488346320
r13            0x7ffff7ff6000	140737354096640
r14            0x0	0
r15            0x30	48
rip            0x7ffff7a2c0bb	0x7ffff7a2c0bb <__GI_raise+203>
eflags         0x246	[ PF ZF IF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0
Stack level 0, frame at 0x7fffffffdb30:
 rip = 0x7ffff7a2c0bb in __GI_raise (../sysdeps/unix/sysv/linux/raise.c:51); saved rip = 0x7ffff7a2df5d
 called by frame at 0x7fffffffdc60
 source language c.
 Arglist at 0x7fffffffda08, args: sig=sig@entry=6
 Locals at 0x7fffffffda08, Previous frame's sp is 0x7fffffffdb30
 Saved registers:
  rip at 0x7fffffffdb28
0x7fffffffda10:	0x00000000	0x00000000	0xf7dd0720	0x00007fff
0x7fffffffda20:	0xf7ffd9d0	0x00007fff	0xf7dd5398	0x00007fff
0x7fffffffda30:	0xf7dd5650	0x00007fff	0x00000008	0x00000030
0x7fffffffda40:	0xffffdf70	0x00007fff	0xffffdeb0	0x00007fff
0x7fffffffda50:	0xf7a68ac0	0x00007fff	0xf7dd0720	0x00007fff
0x7fffffffda60:	0xffffdaf4	0x00007fff	0xf7ddf361	0x00007fff
0x7fffffffda70:	0xf7fd4510	0x00007fff	0x00000008	0x00000030
0x7fffffffda80:	0xffffdfb0	0x00007fff	0xffffdef0	0x00007fff
0x7fffffffda90:	0x7fffffff	0xfffffffe	0xffffffff	0xffffffff
0x7fffffffdaa0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdab0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdac0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdad0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdae0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdaf0:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdb00:	0xffffffff	0xffffffff	0xffffffff	0xffffffff
0x7fffffffdb10:	0xf7ff6000	0x00007fff	0x9bf00700	0xa5566466
0x7fffffffdb20:	0x00000030	0x00000000	0xf7a2df5d	0x00007fff
0x7fffffffdb30:	0x00000020	0x00000000	0x00000000	0x00000000
0x7fffffffdb40:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb50:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb60:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb70:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb80:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffdb90:	0x00000000	0x00000000	0x00000000	0x00000000
