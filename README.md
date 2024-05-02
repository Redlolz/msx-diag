# MSX DIAG

Attempts to diagnose issues in MSX machines.

## FEATURES

* Can (partly) be used in a system with faulty memory
* RAM Test
* VRAM Test
* Memory Monitor

## HOW TO USE

1. Write the ROM file to an (E)EPROM and put it in your MSX where
the BIOS ROM would normally be.

2. Turn on the computer, if you see a menu with various options that means that
the initial checks have passed, the VRAM and the top 8K of the main memory are
good.  If you do not see this menu, go to the troubleshooting section of this
document.

The options on the main menu are all relatively self-explanatory
and the average technician should have no trouble finding their way around the
diagnostic tool.

## TROUBLESHOOTING

### The screen turned from a magenta colour to flashing green or red

You have bad video memory, the flashes of red indicate which bits are faulty.

Quick example, the RAM chip responsible for bit 2 (like this `00000x00`, we
count from zero) is dead which means that the screen will:

* Flash green twice
* Flash red once
* Flash green five times

This information can be used to quickly find the dead RAM chip on the mainboard
of the computer.

### The screen hangs on "TINY RAM TEST" and does not continue

You have bad main memory. The RAM test will show you at what address the fault
occured on and which bits had an unexpected value.

Quick example, you are working on an MSX computer with dynamic RAM and the
RAM test displays a value of `00100000`. This means that the RAM chip connected
to pin D5 of the CPU is most likely dead or not making proper contact with its
socket.

## LICENSE

All code licensed under the GPL-3.0 licence.

[Spleen](https://github.com/fcambus/spleen) font used in `font.png` is
licenced under the 2-clause BSD licence.

Copyright(c) 2024 Redlolz
