### Rename_my_media
Python code for renaming my media for Plex/Jellyfin

This script is to rename files in a spacifc manner.

The struct of your media is supouse to end up like:

Season X (FOLDER)

- SXE01 (MEDIA)

- SXE02 (MEDIA)

- SXE03 (MEDIA)

- SXE04 (MEDIA)

- SXE05 (MEDIA)

This scrip will maintain the extenssion of the original file.

Here are some exemples of changes made:

BEFORE

Top Gear

  Season 10
  
   - T10 EP.1 - Episode 1
   - T10 EP.2 - Episode 2
   - T10 EP.3 - Episode 3

AFTER

Top Gear

  Season 10
  
  - S10E01.mkv
  - S10E02.mkv
  - S10E03.mkv
