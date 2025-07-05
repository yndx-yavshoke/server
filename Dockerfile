FROM oven/bun:1 as base
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy package.json
COPY package.json ./

# Install dependencies
RUN bun install

# Copy source code
COPY . .

# Copy experiments.json (will be overridden by volume mount in production)
COPY experiments.json ./

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

# Start script that waits for DB and runs migrations
COPY start.sh ./
RUN sed -i 's/\r$//' start.sh
RUN chmod +x start.sh

ENTRYPOINT ["bash", "./start.sh"]