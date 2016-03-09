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

* `-d, --dry-run`	=	Disk full threshold (Default 700 (e.g. 70%))
* `-p,--path`	=	Period in seconds between disk threshold checks. The default interval is 60 seconds. Higher quality source media and a smaller disk size require more frequent threshold checks A higher disk threshold (speficied by the user) will also require more frequent checks;
* `-f,--ffprobe-path`	=	Path to the temporary working directory used by the Plex New Transcoder. The transcode_path can be modified from the Plex web through Settings -> Server -> General -> Advanced;

### Credits
I'd like to thank https://github.com/clinton-hall/nzbToMedia/issues/534 for the full script.

### Issues

If you have any problems with or questions about this, please contact me through a [GitHub issue!](/issues).