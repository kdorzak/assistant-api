FROM python:3.13-slim

WORKDIR /app/


ENV PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH" \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONPATH=/app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.4.28 /uv /bin/uv

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project


COPY ./pyproject.toml ./uv.lock /app/
COPY app/ /app/

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync

RUN addgroup --system fastapi && adduser --system --ingroup fastapi fastapi
RUN chown -R fastapi:fastapi /app
USER fastapi

EXPOSE 8080
CMD ["fastapi", "run", "--proxy-headers", "--workers", "4", "main.py", "--port", "8080", "--root-path", "/assistant-api"]