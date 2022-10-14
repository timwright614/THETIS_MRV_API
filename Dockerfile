# Container for building the environment
FROM continuumio/miniconda3

WORKDIR /code

COPY ./environment.yml /code/environment.yml

RUN conda env create -f /code/environment.yml

SHELL ["conda", "run", "-n", "thetis_mrv", "/bin/bash", "-c"]

COPY ./app /code/app

COPY ./data/mrv_df.pkl /code/data/mrv_df.pkl

CMD ["conda", "run", "--no-capture-output", "-n", "thetis_mrv", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
