AS=zasm

msxdiag.rom: main.z80 vdp.z80 ppi.z80 mem.z80 test_vram.z80 test_ram.z80 menu.z80 font.bin
	$(AS) -u -i $< -o $@
	tools/lst2sym.sh main.lst > $@.sym

font.bin: font.png
	python tools/font2bin.py $< $@

.PHONY: run flash clean

run: msxdiag.rom
	~/src/gomsx/gomsx -sys $<

flash: msxdiag.rom
	minipro -p "W27E257@DIP28" -w $<

clean:
	$(RM) *.bin *.rom *.sym
