FROM schlarpc/resin-wpe-python:5

COPY udev-rules/ /etc/udev/rules.d/

COPY ./dependencies.sh /dependencies.sh
RUN sh /dependencies.sh

COPY ./inputSwitch.py /inputSwitch.py

COPY wpe-init /wpe-init
CMD [ "/wpe-init" ]
