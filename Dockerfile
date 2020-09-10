FROM python:3.7

WORKDIR /usr/src/app
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# copy entrypoint.sh
COPY ./entrypoint.sh .

RUN chmod 777 entrypoint.sh
# copy project

# run entrypoint.sh
CMD ["/usr/src/app/entrypoint.sh"]
