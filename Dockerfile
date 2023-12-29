FROM python:3.10.4-alpine3.15

# Instala las dependencias necesarias
RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev cairo-dev cairo

# Configura el entorno
ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo
WORKDIR /app

# Actualiza pip y copia los requisitos
RUN pip install --upgrade pip
COPY ./requirements.txt ./

# Instala los requisitos
RUN pip install -r requirements.txt

# Copia el resto del código de la aplicación
COPY ./ ./

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
