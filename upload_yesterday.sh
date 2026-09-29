#!/bin/bash
yesterday=$(date -d "yesterday" +%F)
python3 extract_daily_sales.py $yesterday $yesterday
