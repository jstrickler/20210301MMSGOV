import PIL.ExifTags
from PIL.ExifTags import TAGS
import exifread
import sys

file = open(sys.argv[1], 'rb')
tags = exifread.process_file(file)

for tag_id in tags:
    tag = TAGS.get(tag_id, tag_id)
    data = tags.get(tag_id)
    print(f"{tag:25}: {data}")