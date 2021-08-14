#!/usr/bin/env python3
# -*- coding: utf-8 -*

import RPi.GPIO as GPIO
from time import sleep

def readadc(adcnum, clockpin, mosipin, misopin, cspin):
	if adcnum > 7 or adcnum < 0:
		return -1
	GPIO.output(cspin, GPIO.HIGH)
	GPIO.output(clockpin, GPIO.LOW)
	GPIO.output(cspin, GPIO.LOW)

	commandout = adcnum
	commandout |= 0x18
	commandout <<= 3
	for i in range(5):
		if commandout & 0x80:
			GPIO.output(mosipin, GPIO.HIGH)
		else:
			GPIO.output(mosipin, GPIO.LOW)
		commandout <<= 1
		GPIO.output(clockpin, GPIO.HIGH)
		GPIO.output(clockpin, GPIO.LOW)
	adcout = 0

	# MCP3008 は 10 bit なので、先頭 null bit を加味した 11 bit 取得 
	for i in range(11):
		GPIO.output(clockpin, GPIO.HIGH)
		GPIO.output(clockpin, GPIO.LOW)
		adcout <<= 1
		if i > 0 and GPIO.input(misopin) == GPIO.HIGH:
			adcout |= 0x1
	GPIO.output(cspin, GPIO.HIGH)
	return adcout

GPIO.setmode(GPIO.BCM)

# 配列を利用
led_pins = (5, 6, 13, 19, 26, 12, 16, 20, 21, 23)
led_stats = [False, False, False, False, False, False, False, False, False, False ]

SPICLK = 11
SPIMOSI = 10
SPIMISO = 9
SPICS = 8

GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICS, GPIO.OUT)

# 一括して出力設定を実施
for pin in led_pins:
	GPIO.setup(pin, GPIO.OUT)

print('初期化開始')
for pin in led_pins:
	GPIO.output(pin, GPIO.HIGH)
sleep(1)
for pin in led_pins:
	GPIO.output(pin, GPIO.LOW)
print('初期化終了')

try:
	while True:
		inputVal0 = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)

    # レベルメーターとして点灯させる範囲を計算する
		# 10 bit の最大値は 1023
		# 今回の表示するパターン数は 11 通りなので、
		# 1023 / 11 = 93 となる
		led_bright_at = int(inputVal0 / 93)
		# print(inputVal0, led_bright_at)

		# 一つずつled_pinsを灯していく
		for i, s in enumerate(led_stats):
			if i < led_bright_at:
				led_stats[i] = True
			else:
				led_stats[i] = False

		for i, pin in enumerate(led_pins):
			GPIO.output(pin, led_stats[i])

		sleep(0.08)
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
