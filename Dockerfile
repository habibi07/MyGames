FROM python:3.9

LABEL author="Krzysztof Gregorowicz"
LABEL description="Prosta aplikacja do zarządzania posiadanymi grami"

WORKDIR /code
ADD . .

# disable cache dir to make image smaller
RUN pip install --no-cache-dir -r requirements.txt 

# TODO: dodać testing stage

EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
