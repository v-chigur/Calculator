#!/bin/bash

while (true); do
	./gen > input
	./parser < input > output1
	./checker < input > output2
	if (diff output1 output2); then
		cat input
	else
		break
	fi
done