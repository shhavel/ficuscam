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

Set up scripts `pic.py` and `post.sh` to run periodically one after another.

[Scheduling tasks with Cron](https://www.raspberrypi.org/documentation/linux/usage/cron.md)

Run crontab: `crontab -e`, and specify `pic.py` to run each hour during the day and `post.sh` 1 minute after:

```sh
0 5-20 * * * /home/pi/ficuscam/pic.py
1 5-20 * * * /home/pi/ficuscam/post.sh
```

Recheck that the scripts are saved in crontab: `crontab -l`

## Troubleshooting

Ensure `pic.py` and `post.sh` both work:

```sh
./pic.py
./post.sh
```
