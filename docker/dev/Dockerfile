FROM oniolalekan/zenobackend-base:latest
MAINTAINER ONI OLALEKAN <olalekan.joseph@gmail.com>

# Install dev/build dependencies
RUN apt-get update && \
    apt-get install python3-dev build-essential -qy libmysqlclient-dev

# Activate virtual environment and install wheel support
RUN . /opt/venv/bin/activate && \
    pip install wheel --upgrade


# PIP environment variables (NOTE: must be set after installing wheel)
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache

# OUTPUT: Build artefacts (Wheels) are output here
VOLUME /wheelhouse

# OUTPUT: Test reports are output here
VOLUME /reports

# Add test entrypoint script
COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

# Set defaults for entrypoint and command string
ENTRYPOINT ["test.sh"]
CMD ["python", "manage.py", "test", "--noinput"]

# Add application source
COPY src /application
WORKDIR /application

# docker build -t zenobackend-dev -f docker/dev/Dockerfile .
#docker run --rm zenobackend-dev
