-----------------------------------------
[![GitHub issues](https://img.shields.io/github/issues/Mirabis/CorruptionCheck.svg)](https://github.com/Mirabis/CorruptionCheck/issues)
[![GitHub forks](https://img.shields.io/github/forks/Mirabis/CorruptionCheck.svg?style=flat-square)](https://github.com/Mirabis/CorruptionCheck/network)
-----------------------------------------
# CorruptionCheck
CorruptionCheck is a small python3 script extracted from nzbToMedia to run a quick corruption check.

```bash

python[3] CorruptionCheck.py -d false -p '/mnt/media' -f '/usr/bin/ffprobe'

```
### Configurable Options

The variables are honored to configure your instance:

* `-d, --dry-run`	=	Dry run, print only - no actual deletion
* `-p,--path`	=	Path to scan for corrupt files.
* `-f,--ffprobe-path`	=	Path to the ffprobe binary (or avprobe)
* `-s, --silent`	=	Only prints warnings & deletions, silent run

### Credits
I'd like to thank https://github.com/clinton-hall/nzbToMedia/issues/534 for the full script.

### Issues

If you have any problems with or questions about this, please contact me through a [GitHub issue!](/issues).