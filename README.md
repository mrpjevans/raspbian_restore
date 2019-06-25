# Raspbian Restore

Self-Healing Raspbian tutorial for MagPi

In MagPi #83 I described the process for creating a Raspbian image that includes a recovery partition. If required, the operator can reset Raspbian back to factory settings (with wi-fi condifured if necessary) with no need to reflash the card or use another computer.

The process is a complicated on, incloving creating a third 'middle' partition containing Raspbian Lite and and a copy of the rootfs image. By running a script the system reconfigures to boot from the recovery partition and overwrite the existing main partition with its backup copy.

The tutorial is intended to give the reader a look at how Linux file systems work. However, it's a lot of work and human error can easily cause a lot of wasted time (believe me, I know!). So, the repo contain not only the code examples form the article but also a complete script that generates the image for you. It is not automatic and will prompt you for various things along the way.

## Usage

Just run the script, ideally from the same working directory. There are no switches, as questions are asked along the way. I may do an automated version one day if there's enough interest.

```bash
./create_raspian_restore
```

The scripts will automatically download the required images (works with Buster) and does all the calculations required. **You will need plenty of disk space**. You're going to download several GB worth of image then create a new image big enough to take the Lite image once and the Full image twice. With Buster the final image is about 12GB.


## Compatibility

Tested on Raspian and Ubuntu. Can be used with docker for other platforms.

## After Creation

You may find you need to extend the third partition using parted or gparted on another machine. To avoid this, find out how many sectors are on your SD card and enter that number when prompted.

## Futures
* It would be nice to restore from a compressed image, saving some space. 
* The full Raspbian Lite is a huge waste of space, look into using something much more lightweight

