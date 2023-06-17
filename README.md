# Mkauthdocs <!-- omit in toc -->
Mkauthdocs is a tool specifically made to implement simple authentication around [mkdocs](www.mkdocs.org) builds.

![Screenshot](img/Screenshot.png)

## Table of contents <!-- omit in toc -->
- [Installation](#installation)
- [Usage](#usage)
- [Functional overview](#functional-overview)
- [License](#license)

## Installation

Mkauthdocs can be directly installed from the [Python Package Index](https://pypi.python.org/pypi/pip)
```sh
pip install mkauthdocs
```

## Usage
```
usage: mkauthdocs.py [-h] [--heading HEADING] username password build_dir

positional arguments:
  username           Username used for authentication
  password           Password used for authentication
  build_dir          Path to build output directory

optional arguments:
  -h, --help         show this help message and exit
  --heading HEADING  Heading on login page (default: 'Login')
```

> **Warning: The password is stored as plain text in the generated php code! Altough this code is only accessible to the server, it is still a risk you should be aware of!**
> Note: This tool **only** applies on **mkdocs builds**, not previews served by `mkdocs serve`

This section attempts to guide the reader trough a typical use case in oder to provide understanding in a context-based environment.

We begin by building our documentation using mkdocs:
```
mkdocs build
```

By default, this will output the generated documentation to the `site/` directory, which will be passed to the tool as an argument (see `build_dir` in [Usage](#usage)).

Now we proceed to add authentication support to the documentation using `mkauthdocs`. The login credentials will be configured the following way:

|Username|`administrator`|
|--------|--------|
|**Password**|`admin`|

*If that isn't the safest password ever ;)*

In addition, we will set the heading of our login page to `Example Reference`. Together, that makes up for the following command:

```bash
mkauthdocs administrator admin site/ --heading "Example Reference"
```

If no feedback has been returned, the documentation should be protected and ready for deployment!

![Screenshot of Result](img/Screenshot2.png)

## Functional overview

As `.htaccess` and `.htpasswd` configurations aren't always a possibility when hosting websites on a proprietary webspace, I was in need of a tool that would allow me to protect the publicly accessible mkdocs build. After endless searching I have only stumbled upon undocumented, incomplete and dated software which ultimately forced me to write my very own minimal tool, providing basic credential authentication to my publicly hosted mkdocs build.

Mkauthdocs implements authentication by injecting a minimally customizable login form into the mkdocs build directory (typically `site/`) and appending PHP session guards at the top of every page.

The login page as well as the session guards are generated from templates which can be found in the [mkauthdocs/templates/](mkauthdocs/templates) directory. If necessary, with a bit of php and html skills those can be customized as desired.

**Example of a generated PHP guard for the index page:**
```php
<?php
  session_start();
  if (! isset($_SESSION['login']) || ! $_SESSION['login']) {
    $dirname = $_SERVER['REQUEST_URI'] ?? '';
    $dirname = preg_replace('/index.php$/', '', $dirname);

    header("Location: ".$dirname."{calibration}login.php?redirect={redirect}");
  }
?>

```

Access to the site is restricted based on the state of the `login` session variable (`$_SESSION['login']`). The user is only granted access if the variable is set to `true`. If the `login` variable is not set or is `false`, the user is redirected to the login page.

To gain access, the user must authenticate themselves on the login page. Upon successful authentication, the `$_SESSION['login']` variable is set to `true`, allowing the user to proceed to the documentation.

If the provided credentials match those set in the generated login page, the user is redirected to the page they originally attempted to access. The destination page after successful login is determined by the `redirect` URL parameter, which is set by the session guards. This mechanism ensures a smooth transition to the desired page following successful authentication.

## License
All files provided by this project fall under the OSS [MIT License](https://en.wikipedia.org/wiki/MIT_License)
```
The MIT License (MIT)

Copyright (c) 2018 Patrick Pedersen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
