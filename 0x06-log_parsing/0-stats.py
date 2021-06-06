#!/usr/bin/python3

import sys
import signal


def log_parsing(functionsize, statuscode):
    print('File size: {}'.format(functionsize))
    for keys, values in sorted(statuscode.items()):
        if values != 0:
            print('{}: {}'.format(keys, values))

status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}

count = 1
function_size = 0

try:
    for line in sys.stdin:
        split1 = line.split()

        if len(split1) > 2:
            file_size = split1[-1]
            status = split1[-2]
            function_size = function_size + int(file_size)


            if status in status_code:
                status_code[status] = status_code[status] + 1


        if count % 10 == 0:
            print('File size: {}'.format(function_size))
            for key, value in sorted(status_code.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

        count = count + 1

except KeyboardInterrupt:
    pass

finally:
    log_parsing(function_size, status_code)
