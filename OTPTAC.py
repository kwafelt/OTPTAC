#!/usr/bin/env python3
import math, random, string

digits = string.digits
digits = str(digits[::-1])
raw = [""]

def generateOTP(init):
  global digits
  num = digits
  length = len(digits)
  OTP = raw[0]
  for i in range(init):
    OTP += num[math.floor(random.random() * length)]
  return OTP

OTP = generateOTP(6)
print(f'\r\n OTP : {OTP}\n')
