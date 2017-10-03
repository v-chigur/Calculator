#!/bin/bash

while (true); do
	./gen.py > input
	./parser < input > output1
	./checker < input > output2
	DIFF=$(diff output1 output2)
	if [ "$DIFF" != "" ]
	then
	    cat input
	    break
	else
		echo -e "ok"
	fi
done