AS=zasm
DEPS=main.z80 \
	libraries/vdp.z80 \
	libraries/ppi.z80 \
	libraries/psg.z80 \
	libraries/mem.z80 \
	init_test_vram.z80 \
	init_test_ram.z80 \
	menu.z80 \
	monitor.z80 \
	ram_test.z80 \
	joystick_test.z80 \
	keyboard_test.z80 \
	joystick.spr \
	keyboard.spr \
	spleen.fnt

msxdiag.rom: $(DEPS)
	$(AS) -u -i $< -o $@
	tools/lst2sym.sh main.lst > $@.sym

%.fnt: %.png
	python tools/font2bin.py $< $@

%.spr: %.png
	python tools/tileset2bin.py $< $@

.PHONY: run flash clean

run: msxdiag.rom
	~/src/gomsx/gomsx -sys $<

flash: msxdiag.rom
	minipro -p "W27E257@DIP28" -w $<

clean:
	$(RM) *.bin *.rom *.sym
