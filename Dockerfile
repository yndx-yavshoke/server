FROM oven/bun:1 AS base
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY package.json ./
RUN bun install

COPY . .

COPY experiments.json ./

COPY start.sh ./
RUN chmod +x start.sh

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

# 👇 лучше всего
CMD ["sh", "start.sh"]
