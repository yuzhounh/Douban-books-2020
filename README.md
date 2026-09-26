# Douban Books 2020: Doulists and Tags

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-D4A017.svg)](LICENSE)

Copyright (C) 2020-2025 Jing Wang

## Overview

This repository preserves a historical collection of Douban book data. It converts the tables from the original project into CSV files with UTF-8 with BOM encoding, making them easy to open and view directly in WPS or Microsoft Office. The counts below describe this dataset, not the current Douban catalog.

📁 [Code](Code)  
The original data and conversion code.

:octocat: [Douban-books-crawler-2020](https://github.com/yuzhounh/Douban-books-crawler-2020)  
The code for crawling the original data from Douban.

## Data access

Open the CSV files directly in WPS or Microsoft Office, or read them using UTF-8 with BOM (`utf-8-sig`). The book CSV files use four fields: `ID` (Douban subject ID), `Rating` (rating), `Votes` (rating count), and `Title` (book title).

[Code](Code) contains the [original data archive](Code/Douban-books-2020.zip) and conversion scripts. The scripts expect the original files and folders relative to the current working directory; downloading the published CSV files does not require running them.

## Datasets

This section contains various book datasets and collections organized by ratings, votes, doulists, and tags.

📊 [Books_1.csv](Books_1.csv)  
Books with rating >= 0.0 and votes >= 0.  
Total number: 288824  

📊 [Books_2.csv](Books_2.csv)  
Books with rating >= 9.0 and votes >= 1000.  
Total number: 1742  

📊 [Books_3.csv](Books_3.csv)  
Books with rating >= 8.5 and votes >= 0.  
Total number: 62028  

📁 [Doulists](Doulists)  
📊 [Doulists_info.csv](Doulists_info.csv)  
The number of doulists: 481

📁 [Tags](Tags)  
📊 [Tags_info.csv](Tags_info.csv)  
The number of tags: 897

## Related projects

- [Douban-books-crawler-2020](https://github.com/yuzhounh/Douban-books-crawler-2020): Python and MATLAB workflow used to collect and process the 2020 results.
- [Douban-books-2017](https://github.com/yuzhounh/Douban-books-2017): Earlier 2017 result snapshot containing 129,193 books.
- [Douban-books-results](https://github.com/yuzhounh/Douban-books-results): Earlier result snapshot containing 34,636 books.
- [douban-books-ranking](https://github.com/yuzhounh/douban-books-ranking): Newer standalone Python implementation with an online ranking and published JSON data.

## License

See [LICENSE](LICENSE) for the GNU General Public License v3.0.

## Contact

Jing Wang  
📧 yuzhounh@163.com
