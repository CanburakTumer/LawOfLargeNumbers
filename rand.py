#!/usr/bin/python
from __future__ import division
from random import randint

def avg(num, arr):
	"calculates the average of given part array"
	sum = 0
	for i in range(0, num):
		sum += arr[i]
#	print sum
#	print arr[0:num]
	return sum/num

def count(rng, num, arr):
	"counts the numbers in rng"
	data = [0]*rng
#old school debug
#	print data
#	print rng
#	print num
#	print arr[0:num]
#end of old school debug
	for i in range(1,rng+1):
#		print i
		for j in range(0,num):
			if arr[j] == i:
				data[i-1] += 1
#				print "true" 
	return data		

dice = []
coin = []

for i in range(1,10001):
	dice.append(randint(1,6))
	coin.append(randint(1,2))

dice10 = count(6, 10, dice)
dice100 = count(6, 100, dice)
dice1000 = count(6, 1000, dice)
dice10000 = count(6, 10000, dice)
diceAvg10 = avg(10, dice)
diceAvg100 = avg(100, dice)
diceAvg1000 = avg(1000, dice)
diceAvg10000 = avg(10000, dice)

coin10 = count(2, 10, coin)
coin100 = count(2, 100, coin)
coin1000 = count(2, 1000, coin)
coin10000 = count(2, 10000, coin)
coinAvg10 = avg(10, coin)
coinAvg100 = avg(100, coin)
coinAvg1000 = avg(1000, coin)
coinAvg10000 = avg(10000, coin)

print "Count for dice roll occurings 10/100/1K/10K"
print dice10
print dice100
print dice1000
print dice10000

print "Average value for dice rolls 10/100/1K/10K"
print diceAvg10
print diceAvg100
print diceAvg1000
print diceAvg10000

print "Count for coin flip occurings 10/100/1K/10K"
print coin10
print coin100
print coin1000
print coin10000

print "Average value for coin flips 10/100/1K/10K"
print coinAvg10
print coinAvg100
print coinAvg1000
print coinAvg10000

#print coin
