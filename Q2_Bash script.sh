#!/bin/sh
for((i=1;i<=100;i++));do mkdir DDM$i ;done
for((i=1;i<=100;i++));do echo -e 'nanoseconds since 1970-01-01 00:00:00 UTC:\n<'`date`'>' > DDM$i/time_till_now.txt ;done
