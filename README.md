# MSX DIAG

Attempts to diagnose issues in MSX machines.

## FEATURES

* RAM Test
* VRAM Test

## HOW TO USE

1. Write the ROM file to an (E)EPROM and put it in your MSX where
the BIOS ROM would normally be.

2. Turn on the computer, if all the checks passed you should see a menu with
various options to test the computer. These are all relatively self-explanatory
and the average technician should have no trouble finding their way around the
diagnostic tool. If you do not see this menu, go to the troubleshooting
section of this document.

## TROUBLESHOOTING

### The screen turned from a magenta colour to flashing green or red

You have bad video memory, the flashes of red indicate which bits are faulty.

Quick example, The RAM chip responsible for bit 2 (like this `00000x00`, we
count from zero) is dead which means that the screen will:

* Flash green twice
* Flash red once
* Flash green five times

This information can be used to quickly find the dead RAM chip on the mainboard
of the computer.

### The screen hangs on "TINY RAM TEST" and does not continue

You have bad main memory.

## LICENSE

All code licensed under the GPL-3.0 licence.

[Spleen](https://github.com/fcambus/spleen) font used in `font.png` is
licenced under the 2-clause BSD licence.

Copyright(c) 2024 Redlolz
