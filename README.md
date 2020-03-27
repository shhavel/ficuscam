# Ficuscam (PicPost)

Simple web camera two-scripts app for Raspberry Pi created to monitor my ficus (home plant) remotelly.

## Description

Script `pic.py` takes a picture [using a standard USB webcam](https://www.raspberrypi.org/documentation/usage/webcams/) with [fswebcam](https://github.com/fsphil/fswebcam) library.

Script `post.sh` makes a git commit with taken pictures and pushes to remote git repository.

## Configuratoin

### Pre requirements

Make sure that both scripts have execute permissions:

```sh
chmod +x pic.py
chmod +x post.sh
```

### Git

Ensure your default user has ability to push to remote repo.

### Scheduling tasks with Cron

Set up script `pic.py` to run each hour and `post.sh` in 5 minutes after `pic.py`.

[Scheduling tasks with Cron](https://www.raspberrypi.org/documentation/linux/usage/cron.md)

Run crontab: `crontab -e`, and specify `pic.py` to run each hour and `post.sh` 5 minutes after:

```sh
0 * * * * /home/pi/ficuscam/pic.py
5 * * * * /home/pi/ficuscam/post.sh
```

Recheck that the scripts are saved in crontab: `crontab -l`

Or `pic.py` run each 10 minutes and `post.sh` one minute since then every time:

```sh
*/10 * * * * /home/pi/ficuscam/pic.py
1,11,21,31,41,51 * * * * /home/pi/ficuscam/post.sh
```
