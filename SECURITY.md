# Security Policy

## Supported versions

This project supports the following Python versions and conforms to the Django release note.

| Python version                                                   | Supported          | Security Support Deadline |
|------------------------------------------------------------------|--------------------|---------------------------|
| 3.10.x (Ubuntu LTS 22.04)                                        | :white_check_mark: | 04 Oct 2026               |
| 3.11.x (Debian Bookworm)                                         | :white_check_mark: | 24 Oct 2027               |
| 3.12.x (Ubuntu 24.04 LTS and others)                             | :white_check_mark: | Oct 2028                  |
| 3.13.x (Arch Linux and others)                                   | :white_check_mark: | Oct 2030                  |

More in [Status of Python Versions](https://devguide.python.org/versions/)

## Notes

- Python compatibility: [Django](https://www.djangoproject.com/start/overview/) 4.2 supports Python 3.8, 3.9, 3.10, 3.11, 3.12 and 3.13 (as of Django 4.2.8) (release note at the link below).
- Highly recommend and only officially support the latest release of each series.
- [Django 4.2](https://docs.djangoproject.com/en/4.2/releases/4.2/) not work with [PostgreSQL](https://www.postgresql.org/) 11 and work with 12 or higher.
- [Psycopg2](https://github.com/psycopg/psycopg2) updated version to 2.9.6 (deprecated [Release notes 4.2](https://docs.djangoproject.com/en/5.0/releases/4.2/#psycopg-3-support)).
- [Psycopg](https://github.com/psycopg/psycopg) updated version to 3.1.18.
- Last [dependencies](https://github.com/leandrocunha526/client-manager/commit/a8ca0a6cd54e264fce9c5f1496f5053d382f949d) update: Tuesday, April 11th, 2023 by commit (continuously improves).
- [Extended support for Django 2.2 ended in April 2022 and the maintainers recommended upgrading to the latest version](https://www.djangoproject.com/weblog/2022/apr/11/security-releases/).
- [Pillow](https://github.com/python-pillow/Pillow): [9.5.0 works with Python 3.11 and older versions (< 9.3.0) not work](https://github.com/python-pillow/Pillow/issues/6575).
- [End of life dates for supported database versions](https://code.djangoproject.com/wiki/SupportedDatabaseVersions).
- Is highly recommend the update to versions with support.
- There is no way to guarantee compatibility with Python 3.11 to [Django 2.2.28](https://docs.djangoproject.com/en/4.1/releases/2.2/) (archived in [django2.2-archived](https://github.com/leandrocunha526/client-manager/tree/django2.2-archived) branch). Upstream has ended extended support as mentioned above.
- Fixed compatibility with Python version 3.12, updated Django for 4.2.11, psycopg for 3.1.18 and see recent commit in [requirements.txt](requirements.txt) for see new changes.
- Fixed compatibility with Python version 3.13 and updated dependencies.

## Fixing a vulnerability

We have a database of vulnerabilities audited by experts (see [database advisories](https://github.com/advisories/)) that affect the current version of Django and other dependencies the project is using with CI testing to test (fail if return code 1 with warnings or errors) compatibility with the version (all versions listed above) that fixes this vulnerability to ensure that the project can still be run and used normally.  
The migration to Django 4.2 was a milestone for this project which back to support with security fixes until April 2026.  
[Dependabot](https://github.com/dependabot) is authorized to open pull requests to help keep the project safe.  
About security flaw in the code of this repository, from the moment it was diagnosed with tests, will be resolved followed by new tests and then inserted in the code with commit reporting details of this change.  
Pull request is accepted with commit in other branch.  
And others security trackers: [Mitre](https://cve.mitre.org/), [posts about security fixes in Django releases](https://www.djangoproject.com/weblog/) and [NIST](https://nvd.nist.gov/)
