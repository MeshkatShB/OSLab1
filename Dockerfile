FROM python:2
COPY . .
CMD [ "python", "./SpeedRace.py" ]