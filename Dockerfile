FROM oven/bun:1 as base
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Copy package.json
COPY package.json ./

# Install dependencies
RUN bun install

# Copy source code
COPY . .

# Copy experiments.json
COPY experiments.json ./

COPY start.sh /usr/src/app/start.sh
RUN chmod +x /usr/src/app/start.sh
WORKDIR /usr/src/app


EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

CMD ["./start.sh"]

