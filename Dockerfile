FROM python:3.8-slim-buster

COPY ./ home/
RUN cd home/

RUN python -m pip install --upgrade pip
RUN pip install Dash
RUN pip install pandas

RUN pip freeze >> requirements.txt
RUN touch app.py
RUN pip install -r requirements.txt

CMD [ "python", "app.py"]
