FROM python
RUN pip install openai && \
pip install discord
WORKDIR /app
COPY . .
ENTRYPOINT ["python","main.py"]