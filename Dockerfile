FROM python:3

ENV api_url http://ndi.eliott.tech
ENV slack_token
ENV name westebot

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python ./slack_integration.py --url $api_url --name $name --token $slack_token
