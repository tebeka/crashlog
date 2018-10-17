# crashlog 0.1.0

[![Build Status](https://travis-ci.org/tebeka/crashlog.svg?branch=master)](https://travis-ci.org/tebeka/crashlog)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Send email and log to file when there's an uncaught exception in your code


# Install

    pip install crashlog


# Usage
    
```python
import crashlog

crashlog.install(email=['bugs@looney.org'], logfile='/path/to/log.txt')
```

For email to work, you need to set `SMTP_SERVER` environment variable and
optionally `SMTP_USER` and `SMTP_PASSWORD`.

Contact
=======
Miki Tebeka <miki.tebeka@gmail.com>

Bug reports go [here][bugs].


[bugs]: https://github.com/tebeka/crashlog/issues
