0x03. Log Parsing
---
script that reads input data from standard input line by line in a specific format, computes metrics, and outputs the statistics for every 10 lines and/or keyboard interruption. The script will calculate the total file size and the number of lines by status code (200, 301, 400, 401, 403, 404, 405, and 500) and print them in ascending order. If a status code doesn't appear or is not an integer, nothing will be printed for that code.
