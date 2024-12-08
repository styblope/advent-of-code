#!/bin/sh

if [ !$(date +%m) == "12" ]; then
  echo "It's not Advent time! Exiting."
  exit 1
fi

SESSION=53616c7465645f5fdd986f72d1c9537645b63795c9641ebb78620a5ea82323f0cc8e47a08de27647d53adb7d5cc85b9fb009d3fb8a02bb4550aa7f313b3993f6

YEAR=$(date +%Y)

if [[ $1 == "" ]]; then
  DATE=$(date)
else
  DATE="Dec $1"
fi

DAY_PADDED=$(date -d"$DATE" +%d)
DAY_SHORT=$(date -d"$DATE" +%e | xargs)
DIR="day$DAY_PADDED"

echo "creating $DIR directory"
mkdir -p $DIR

echo "copying template"
FILE="$DIR.py"
cp template.py $DIR/$FILE

echo "downloading input"
curl -s -b session=$SESSION -o $DIR/input \
  "https://adventofcode.com/$YEAR/day/$DAY_SHORT/input"

cd $DIR
