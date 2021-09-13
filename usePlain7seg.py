#!/usr/bin/env python3
# -*- coding: utf-8 -*

import RPi.GPIO as GPIO
from time import sleep

digitPin01 = 8
segmentPinA = 7
segmentPinB = 21
segmentPinC = 19
segmentPinD = 6
segmentPinE = 5
segmentPinF = 12
segmentPinG = 26
segmentPinDP = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(digitPin01, GPIO.OUT)
GPIO.setup(segmentPinA, GPIO.OUT)
GPIO.setup(segmentPinB, GPIO.OUT)
GPIO.setup(segmentPinC, GPIO.OUT)
GPIO.setup(segmentPinD, GPIO.OUT)
GPIO.setup(segmentPinE, GPIO.OUT)
GPIO.setup(segmentPinF, GPIO.OUT)
GPIO.setup(segmentPinG, GPIO.OUT)
GPIO.setup(segmentPinDP, GPIO.OUT)

try:
    while True:
        GPIO.output(digitPin01, GPIO.HIGH)

        # 0 出力
        GPIO.output(segmentPinA, GPIO.LOW)
        GPIO.output(segmentPinB, GPIO.LOW)
        GPIO.output(segmentPinC, GPIO.LOW)
        GPIO.output(segmentPinD, GPIO.LOW)
        GPIO.output(segmentPinE, GPIO.LOW)
        GPIO.output(segmentPinF, GPIO.LOW)
        GPIO.output(segmentPinG, GPIO.HIGH)
        GPIO.output(segmentPinDP, GPIO.HIGH)
        sleep(0.5)

        # 1 出力
        GPIO.output(segmentPinA, GPIO.HIGH)
        GPIO.output(segmentPinB, GPIO.LOW)
        GPIO.output(segmentPinC, GPIO.LOW)
        GPIO.output(segmentPinD, GPIO.HIGH)
        GPIO.output(segmentPinE, GPIO.HIGH)
        GPIO.output(segmentPinF, GPIO.HIGH)
        GPIO.output(segmentPinG, GPIO.HIGH)
        GPIO.output(segmentPinDP, GPIO.HIGH)
        sleep(0.5)

        # 2 出力
        GPIO.output(segmentPinA, GPIO.LOW)
        GPIO.output(segmentPinB, GPIO.LOW)
        GPIO.output(segmentPinC, GPIO.HIGH)
        GPIO.output(segmentPinD, GPIO.LOW)
        GPIO.output(segmentPinE, GPIO.LOW)
        GPIO.output(segmentPinF, GPIO.HIGH)
        GPIO.output(segmentPinG, GPIO.LOW)
        GPIO.output(segmentPinDP, GPIO.HIGH)
        sleep(0.5)

        # 3 出力
        GPIO.output(segmentPinA, GPIO.LOW)
        GPIO.output(segmentPinB, GPIO.LOW)
        GPIO.output(segmentPinC, GPIO.LOW)
        GPIO.output(segmentPinD, GPIO.LOW)
        GPIO.output(segmentPinE, GPIO.HIGH)
        GPIO.output(segmentPinF, GPIO.HIGH)
        GPIO.output(segmentPinG, GPIO.LOW)
        GPIO.output(segmentPinDP, GPIO.HIGH)
        sleep(0.5)

        # 4 出力
        GPIO.output(segmentPinA, GPIO.HIGH)
        GPIO.output(segmentPinB, GPIO.LOW)
        GPIO.output(segmentPinC, GPIO.LOW)
        GPIO.output(segmentPinD, GPIO.HIGH)
        GPIO.output(segmentPinE, GPIO.HIGH)
        GPIO.output(segmentPinF, GPIO.LOW)
        GPIO.output(segmentPinG, GPIO.LOW)
        GPIO.output(segmentPinDP, GPIO.HIGH)
        sleep(0.5)

        # 5 出力
        GPIO.output(segmentPinA, GPIO.LOW)
        GPIO.output(segmentPinB, GPIO.HIGH)
        GPIO.output(segmentPinC, GPIO.LOW)
        GPIO.output(segmentPinD, GPIO.LOW)
        GPIO.output(segmentPinE, GPIO.HIGH)
        GPIO.output(segmentPinF, GPIO.LOW)
        GPIO.output(segmentPinG, GPIO.LOW)
        GPIO.output(segmentPinDP, GPIO.HIGH)
        sleep(0.5)

        # 6 出力
        GPIO.output(segmentPinA, GPIO.LOW)
        GPIO.output(segmentPinB, GPIO.HIGH)
        GPIO.output(segmentPinC, GPIO.LOW)
        GPIO.output(segmentPinD, GPIO.LOW)
        GPIO.output(segmentPinE, GPIO.LOW)
        GPIO.output(segmentPinF, GPIO.LOW)
        GPIO.output(segmentPinG, GPIO.LOW)
        GPIO.output(segmentPinDP, GPIO.HIGH)
        sleep(0.5)

        # 7 出力
        GPIO.output(segmentPinA, GPIO.LOW)
        GPIO.output(segmentPinB, GPIO.LOW)
        GPIO.output(segmentPinC, GPIO.LOW)
        GPIO.output(segmentPinD, GPIO.HIGH)
        GPIO.output(segmentPinE, GPIO.HIGH)
        GPIO.output(segmentPinF, GPIO.LOW)
        GPIO.output(segmentPinG, GPIO.HIGH)
        GPIO.output(segmentPinDP, GPIO.HIGH)
        sleep(0.5)

        # 8 出力
        GPIO.output(segmentPinA, GPIO.LOW)
        GPIO.output(segmentPinB, GPIO.LOW)
        GPIO.output(segmentPinC, GPIO.LOW)
        GPIO.output(segmentPinD, GPIO.LOW)
        GPIO.output(segmentPinE, GPIO.LOW)
        GPIO.output(segmentPinF, GPIO.LOW)
        GPIO.output(segmentPinG, GPIO.LOW)
        GPIO.output(segmentPinDP, GPIO.HIGH)
        sleep(0.5)

        # 9 出力
        GPIO.output(segmentPinA, GPIO.LOW)
        GPIO.output(segmentPinB, GPIO.LOW)
        GPIO.output(segmentPinC, GPIO.LOW)
        GPIO.output(segmentPinD, GPIO.LOW)
        GPIO.output(segmentPinE, GPIO.HIGH)
        GPIO.output(segmentPinF, GPIO.LOW)
        GPIO.output(segmentPinG, GPIO.LOW)
        GPIO.output(segmentPinDP, GPIO.HIGH)
        sleep(0.5)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
