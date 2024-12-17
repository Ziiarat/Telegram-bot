FROM python:3.10-slim 
ENV TOKEN='7734287293:AAGN3L6dcS16MeoxMSVZNzpcR-0AgtO2tuE'
COPY . .
RUN pip install -r requirements.txt 
ENTRYPOINT ["python", "bot.py"]