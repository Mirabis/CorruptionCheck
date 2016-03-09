# All credits to https://github.com/clinton-hall/nzbToMedia/issues/534

import argparse
import json
import os
import platform
import subprocess
import sys

####
## Accept Arguments
####
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dry-run', default=True, type=bool,help="Dry run, print only - no actual deletion")
parser.add_argument('-p', '--path', default='.', type=str, help="Path to scan for corrupt files.")
parser.add_argument('-f', '--ffprobe-path', default='/usr/bin/ffprobe', type=str,help="Path to the ffprobe binary")
args = parser.parse_args()



FFPROBE = args.ffprobe_path

if not FFPROBE:
    if platform.system() != 'Windows':
        try:
            FFPROBE = subprocess.Popen(['which', 'ffprobe'], stdout=subprocess.PIPE).communicate()[0].strip()
        except: pass
        if not FFPROBE:
            try:
                FFPROBE = subprocess.Popen(['which', 'avprobe'], stdout=subprocess.PIPE).communicate()[0].strip()
            except: pass
    if not FFPROBE:
        print("[WARNING] Failed to locate ffprobe!")
        sys.exit(0)

def isVideoGood(videofile):
    fileNameExt = os.path.basename(videofile)
    fileName, fileExt = os.path.splitext(fileNameExt)
    disable = False
    if fileExt not in ['.mkv','.avi','.divx','.xvid','.mov','.wmv','.mp4','.mpg','.mpeg','.vob','.iso','.ts'] or not FFPROBE:
        return True

    print("[INFO] Checking [{0}] for corruption, please stand by ...".format(fileNameExt))
    video_details, result = getVideoDetails(videofile)

    if result != 0:
        print("[Error] FAILED: [%s] is corrupted!" % (fileNameExt))
        return False
    if video_details.get("error"):
        print ("[INFO] FAILED: [%s] returned error [%s]." % (fileNameExt, str(video_details.get("error"))))
        return False
    if video_details.get("streams"):
        videoStreams = [item for item in video_details["streams"] if item["codec_type"] == "video"]
        audioStreams = [item for item in video_details["streams"] if item["codec_type"] == "audio"]
        if len(videoStreams) > 0 and len(audioStreams) > 0:
            print( "[INFO] SUCCESS: [%s] has no corruption." % (fileNameExt))
            return True
        else:
            print ("[INFO] FAILED: [%s] has %s video streams and %s audio streams. Assume corruption." % (fileNameExt, str(len(videoStreams)), str(len(audioStreams))))
            return False

def getVideoDetails(videofile):
    video_details = {}
    result = 1
    if not FFPROBE:
        return video_details, result
    if 'avprobe' in FFPROBE:
        print_format = '-of'
    else:
        print_format = '-print_format'
    try:
        command = [FFPROBE, '-v', 'quiet', print_format, 'json', '-show_format', '-show_streams', '-show_error', videofile]
        proc = subprocess.Popen(command, stdout=subprocess.PIPE)
        out, err = proc.communicate()
        result = proc.returncode
        video_details = json.loads(out)
    except: pass
    if not video_details:
        try:
            command = [FFPROBE, '-v', 'quiet', print_format, 'json', '-show_format', '-show_streams', videofile]
            proc = subprocess.Popen(command, stdout=subprocess.PIPE)
            out, err = proc.communicate()
            result = proc.returncode
            video_details = json.loads(out)
        except:
            print("[ERROR] Checking [%s] has failed" % (videofile))
    return video_details, result


def corruption_check():
    corrupt = False
    num_files = 0
    good_files = 0
    for dir, dirnames, filenames in os.walk(os.environ['NZBPP_DIRECTORY']):
        for filename in filenames:
            filepath = os.path.join(dir, filename)
            num_files += 1
            if isVideoGood(filepath):
                good_files += 1
            else:
                mode='file'
                xxp=filepath
                os.remove(filepath)
                if not os.listdir(dir):
                    mode='dir'
                    xxp=dir
                    os.rmdir(dir)
                print("[INFO] Removing {0} at {1}".format(mode,xxp))
    if num_files > 0 and good_files < num_files:
        print ("[INFO] Corrupt video file found.")
        corrupt = True
    return corrupt

if __name__ == "__main__":
    corrupt = corruption_check()
    if not corrupt:
        sys.exit(1)
