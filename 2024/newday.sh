#!/bin/sh
if [ !$(date +%m) == "12" ]; then
  echo "It's not Advent time! Exiting."
  exit 1
fi

SESSION=$(cat session)

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
cp -n template.py $DIR/$FILE
sed -i -e "s|DD|$DAY_SHORT|" $DIR/$FILE
sed -i -e "s|YYYY|$YEAR|" $DIR/$FILE

echo "downloading input"
curl -s -b session="$SESSION" -o "$DIR/input" \
  "https://adventofcode.com/$YEAR/day/$DAY_SHORT/input"

cd $DIR
