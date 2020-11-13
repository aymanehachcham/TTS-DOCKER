# Pulling original image: python-alpine (lightweight image)
FROM python:3.8-alpine

# able to run the scripts folder from wihtin the shell of the container, because with add them to the virtual PATH
ENV PATH="/scripts:${PATH}"

# Copy requirements, install nginx dependencies and requirements for the project
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cahe --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp

# create the tts_app, and copy the ttsApi locally to the container
RUN mkdir /tts_app
COPY ./ttsApi /tts_app
WORKDIR /tts_app
COPY ./scripts /scripts

# Change the rights of the scripts, adding execution right
RUN chmod +x /scripts/*

# create the media and audio folders to store the static audios
RUN mkdir -p /vol/media/audio
RUN mkdir -p /vol/media/

# Add virtual user to the container, to avoid running the docker image as a default root user
RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/media
USER user

# Run the entrypoint
CMD ["entrypoint.sh"]

